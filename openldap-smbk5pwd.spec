%{!?ldflags: %global ldflags -Wl,-z,relro -Wl,-O1}

%global openldap openldap%{?olmajor}

Name:       %openldap-smbk5pwd
Version:    2.4.26
Release:    %mkrel 1
Summary:    OpenLdap smbk5pwd overlay
License:    Artistic
Group: 		System/Servers
URL: 		http://www.openldap.org
# the source is created as:
# tar cvjf openldap-smbk5pwd-2.4.24.tar.bz2 openldap-2.4.24/contrib
Source0: 	openldap-smbk5pwd-%{version}.tar.bz2
BuildRequires: heimdal-devel
BuildRequires: %openldap-devel = %{version}
BuildRequires: tcp_wrappers-devel
BuildRequires: libtool
Requires:   %openldap-servers = %{version}
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package contains a slapd overlay, smbk5pwd, that extends the
PasswordModify Extended Operation to update Kerberos keys and Samba
password hashes for an LDAP user.

Note that this package is built with Heimdal support, and requires a working
Heimdal KDC configuration. If you only need support for changing Samba password 
hashes, you can use the 'smbpwd.so' copy provided in openldap-servers (just use 
'moduleload smbpwd.so' instead of 'moduleload smbk5pwd.so) which is identical
except that it is built without Heimdal support.

%prep
%setup -q -n openldap-%{version}/contrib/slapd-modules/smbk5pwd

%build
make \
    OPT="%optflags %ldflags" \
    LIBTOOL=%{_bindir}/libtool \
    HEIMDAL_LIB="-L%{_libdir} -L%{_libdir}/heimdal -lkrb5 -lkadm5srv" \
    LDAP_INC="-I%{_includedir}/%openldap/include -I%{_includedir}/%openldap/slapd"

%install
rm -rf %{buildroot}
%makeinstall_std moduledir=%{_libdir}/%openldap LIBTOOL=%{_bindir}/libtool

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/%openldap/*
