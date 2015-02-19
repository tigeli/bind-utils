Summary: DNS (Domain Name System) server
Name: bind-utils
Version: 9.10.1
Release: P1
License: BSD-like
Group: System Environment/Daemons
URL: http://www.isc.org/products/BIND/

Source: %{name}-%{version}.tar.gz

BuildRequires: openssl-devel

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.

%prep
# Adjusting %%setup since git-pkg unpacks to src/
# %%setup -q
%setup -q -n src

%build
%configure --with-libtool
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

%make_install
make DESTDIR=%{buildroot} -C bin/dig install

%{__rm} -rf %{buildroot}/%{_mandir}
%{__rm} -rf %{buildroot}/usr/{sbin,include}
%{__rm} -rf %{buildroot}/etc
%{__rm} -rf %{buildroot}/usr/bin/bind9-config
%{__rm} -rf %{buildroot}/usr/bin/delv
%{__rm} -rf %{buildroot}/usr/bin/isc-config.sh
%{__rm} -rf %{buildroot}/usr/lib/libirs.so*

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
/usr/bin/dig
/usr/bin/host
/usr/bin/nslookup
/usr/bin/nsupdate
/usr/lib/*.so
/usr/lib/*.so.*
