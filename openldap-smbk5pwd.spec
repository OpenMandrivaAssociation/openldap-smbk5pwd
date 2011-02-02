%{!?ldflags: %global ldflags -Wl,-z,relro -Wl,-O1}

Name:       openldap%{?olmajor}-smbk5pwd
Version:    2.4.22
Release:    %mkrel 1
Summary:    OpenLdap smbk5pwd overlay
License:    Artistic
Group: 		System/Servers
URL: 		http://www.openldap.org
Source0: 	openldap-smbk5pwd-%{version}.tar.bz2
BuildRequires: heimdal-devel
BuildRequires: openldap%{?olmajor}-devel >= 2.4.8
BuildRequires: tcp_wrappers-devel
BuildRequires: libtool
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
    LDAP_INC="-I%{_includedir}/openldap%{?olmajor}/include -I%{_includedir}/openldap%{?olmajor}/slapd"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/openldap%{?olmajor}
cp  .libs/smbk5pwd.so* %{buildroot}/%{_libdir}/openldap%{?olmajor}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/openldap%{?olmajor}/*
