#
Summary:	GSM daemon for OpenMoko
Name:		gsmd
Version:	0.0.0.2352
Release:	0.1
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	76b364697bd4bac52a45cb08416a35ea
URL:		http://openmoko.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	lib%{name} = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSM daemon for OpenMoko

%package -n lib%{name}
Summary:	libgsmd library
Group:		Development/Libraries

%description -n lib%{name}
Libraries for OpenMoko GSM Daemon.

%package -n lib%{name}-devel
Summary:	Header files for libgsmd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgsmd
Group:		Development/Libraries
Requires:	lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Header files for libgsmd library.

%description -n lib%{name}-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgsmd.

%package -n lib%{name}-static
Summary:	Static libgsmd library
Summary(pl.UTF-8):	Statyczna biblioteka libgsmd
Group:		Development/Libraries
Requires:	lib%{name}-devel = %{version}-%{release}

%description -n lib%{name}-static
Static libgsmd library.

%description -n lib%{name}-static -l pl.UTF-8
Statyczna biblioteka libgsmd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n lib%{name} -p /sbin/ldconfig
%postun	-n lib%{name} -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt doc
%attr(755,root,root) %{_sbindir}/gsmd

%files -n lib%{name}
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-machine_generic.so.0.0.0
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-machine_tihtc.so.0.0.0
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_qc.so.0.0.0
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_ti.so.0.0.0
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_tihtc.so.0.0.0
%attr(755,root,root) %{_libdir}/libgsmd.so.0.0.0

%files -n lib%{name}-devel
%attr(755,root,root) %{_bindir}/libgsmd-tool
%{_includedir}/gsmd
%{_includedir}/libgsmd
%{_libdir}/gsmd/libgsmd-machine_generic.la
%{_libdir}/gsmd/libgsmd-machine_tihtc.la
%{_libdir}/gsmd/libgsmd-vendor_qc.la
%{_libdir}/gsmd/libgsmd-vendor_ti.la
%{_libdir}/gsmd/libgsmd-vendor_tihtc.la
%{_libdir}/libgsmd.la
%{_pkgconfigdir}/libgsmd.pc

%files -n lib%{name}-static
%{_libdir}/gsmd/libgsmd-machine_generic.a
%{_libdir}/gsmd/libgsmd-machine_tihtc.a
%{_libdir}/gsmd/libgsmd-vendor_qc.a
%{_libdir}/gsmd/libgsmd-vendor_ti.a
%{_libdir}/gsmd/libgsmd-vendor_tihtc.a
%{_libdir}/libgsmd.a
