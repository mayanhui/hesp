Summary:snappy libary written by kubo(http://github.com/kubo/snzip) packaged by Xianglei
Name: snappy
Version: 1.1.0
Release: 1
License: New BSD
Group: System Environment
Packager: Xianglei
BuildRequires: make gcc-c++ zlib
Source: snappy-1.1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Url: http://www.phphiveadmin.net
BuildArchitectures: x86_64
Requires: zlib

%description
Snappy is a compress/decompress cli tool

%prep
%setup -q

%build
export DESTDIR=%{buildroot}
%configure --prefix=/usr --libdir=/usr/lib --includedir=/usr/include --datarootdir=/usr/share --sbindir=/usr/sbin --libexecdir=/usr/libexec --mandir=/usr/man
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALLDIRS=vendor
 
%post
/sbin/ldconfig > /dev/null

%postun
/sbin/ldconfig > /dev/null

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
/usr/include/snappy-c.h
/usr/include/snappy-sinksource.h
/usr/include/snappy-stubs-public.h
/usr/include/snappy.h
/usr/lib/libsnappy.a
/usr/lib/libsnappy.la
/usr/lib/libsnappy.so
/usr/lib/libsnappy.so.1
/usr/lib/libsnappy.so.1.1.4
/usr/share/doc/snappy/COPYING
/usr/share/doc/snappy/ChangeLog
/usr/share/doc/snappy/INSTALL
/usr/share/doc/snappy/NEWS
/usr/share/doc/snappy/README
/usr/share/doc/snappy/format_description.txt
/usr/share/doc/snappy/framing_format.txt
