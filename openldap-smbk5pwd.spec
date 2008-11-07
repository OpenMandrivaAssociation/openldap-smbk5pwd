Name:       openldap-smbk5pwd
Version:    2.4.8
Release:    %mkrel 5
Summary:    OpenLdap smbk5pwd overlay
License:    Artistic
Group: 		System/Servers
URL: 		http://www.openldap.org
Source0: 	openldap-smbk5pwd-%{version}.tar.gz
Patch0:     openldap-smbk5pwd-2.4.8-dont-use-internal-functions.patch
Patch1:     openldap-smbk5pwd-2.4.8-fix-password-termination.patch
Patch2:     openldap-2.4.12-its5766.patch
BuildRequires: heimdal-devel
BuildRequires: openldap-devel >= 2.4.8
BuildRequires: tcp_wrappers-devel
BuildRequires: libtool
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package contains a slapd overlay, smbk5pwd, that extends the
PasswordModify Extended Operation to update Kerberos keys and Samba
password hashes for an LDAP user.

%prep
%setup -q -n smbk5pwd
%patch0 -p 0
%patch1 -p 0
%patch2 -p 3

%build
make \
    libdir=%{_libdir} \
    LIBTOOL=%{_bindir}/libtool \
    LDAP_INC="-I%{_includedir}/openldap/include -I%{_includedir}/openldap/slapd"

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/openldap
cp  .libs/smbk5pwd.so* %{buildroot}/%{_libdir}/openldap

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/openldap/*
