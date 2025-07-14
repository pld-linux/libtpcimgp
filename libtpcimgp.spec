Summary:	PET Image Processing library
Summary(pl.UTF-8):	Biblioteka PET Image Processing
Name:		libtpcimgp
Version:	1.3.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.turkupetcentre.net/software/libsrc/%{name}_%(echo %{version} | tr . _)_src.zip
# Source0-md5:	dab98428b67a01d2fd937a99040016bf
Patch0:		%{name}-shared.patch
URL:		http://www.turkupetcentre.net/software/libdoc/libtpcimgp/
BuildRequires:	libtpcimgio-devel >= 1.3.0
BuildRequires:	unzip
Requires:	libtpcimgio >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PET Image Processing library by Turku PET Centre.

%description -l pl.UTF-8
PET Image Processing - biblioteka przetwarzania obrazów Turku PET
Centre.

%package devel
Summary:	Header files for libtpcimgp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libtpcimgp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libtpcimgio-devel >= 1.3.0

%description devel
Header files for libtpcimgp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libtpcimgp.

%package static
Summary:	Static libtpcimgp library
Summary(pl.UTF-8):	Statyczna biblioteka libtpcimgp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtpcimgp library.

%description static -l pl.UTF-8
Statyczna biblioteka libtpcimgp.

%prep
%setup -q -n %{name}_%(echo %{version} | tr . _)
%patch -P0 -p1

%build
%{__make} libtpcimgp.la \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -std=gnu99 -Wall -I/usr/include/tpc -Iinclude \$(INCLUDE) \$(ANSI)" \
	LDFLAGS="%{rpmldflags}" \
	PET_LIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} libinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	PET_LIB=%{_libdir}

install -d $RPM_BUILD_ROOT%{_includedir}/tpc
install include/*.h $RPM_BUILD_ROOT%{_includedir}/tpc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc History Readme TODO
%attr(755,root,root) %{_libdir}/libtpcimgp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtpcimgp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtpcimgp.so
%{_libdir}/libtpcimgp.la
%{_includedir}/tpc/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtpcimgp.a
