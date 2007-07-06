Summary:	GSM daemon for OpenMoko
Summary(pl.UTF-8):	Demon GSM dla OpenMoko
Name:		gsmd
Version:	0.0.0.2352
Release:	0.1
License:	LGPL v2.1
Group:		Daemons
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	76b364697bd4bac52a45cb08416a35ea
URL:		http://openmoko.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
Requires:	lib%{name} = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSM daemon for OpenMoko.

%description -l pl.UTF-8
Demon GSM dla OpenMoko.

%package -n lib%{name}
Summary:	libgsmd library
Summary(pl.UTF-8):	Biblioteka libgsmd
Group:		Libraries

%description -n lib%{name}
OpenMoko GSM Daemon library.

%description -n lib%{name} -l pl.UTF-8
Biblioteka demona OpenMoko GSM.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/gsmd/libgsmd-*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n lib%{name} -p /sbin/ldconfig
%postun	-n lib%{name} -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt doc
%attr(755,root,root) %{_sbindir}/gsmd
%dir %{_libdir}/gsmd
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-machine_generic.so*
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-machine_tihtc.so*
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_qc.so*
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_ti.so*
%attr(755,root,root) %{_libdir}/gsmd/libgsmd-vendor_tihtc.so*

%files -n lib%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgsmd.so.*.*.*

%files -n lib%{name}-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libgsmd-tool
%attr(755,root,root) %{_libdir}/libgsmd.so
%{_libdir}/libgsmd.la
%{_includedir}/gsmd
%{_includedir}/libgsmd
%{_pkgconfigdir}/libgsmd.pc

%files -n lib%{name}-static
%defattr(644,root,root,755)
%{_libdir}/libgsmd.a
