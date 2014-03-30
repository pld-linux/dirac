#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	static_libs	# don't build static libraries

Summary:	General purpose video codec
Summary(pl.UTF-8):	Kodek obrazu ogólnego przeznaczenia
Name:		dirac
Version:	1.0.2
Release:	5
License:	MPL v1.1 or GPL v2 or LGPL v2.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/dirac/%{name}-%{version}.tar.gz
# Source0-md5:	a57c2c5e58062d437d9ab13dffb28f0f
Patch0:		%{name}-am.patch
URL:		http://www.bbc.co.uk/rd/projects/dirac/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-metafont
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.map *.dot

%description
Dirac is a general-purpose video codec aimed at resolutions from QCIF
(180x144) to HDTV (1920x1080) progressive or interlaced. It uses
wavelets, motion compensation and arithmetic coding.

%description -l pl.UTF-8
Dirac jest kodekiem ogólnego przeznaczenia dla obrazu o
rozdzielczościach od QCIF (180x144) do HDTV (1920x1080). Kodek ten
wykorzystuje fale elementarne (wavelets), kompensację ruchu (motion
compensation) oraz kodowanie arytmetyczne (arithmetic coding).

%package libs
Summary:	Libraries for dirac codec
Summary(pl.UTF-8):	Biblioteki kodeka dirac
Group:		Libraries
Conflicts:	dirac < 1.0.2-3

%description libs
Dirac is a general-purpose video codec aimed at resolutions from QCIF
(180x144) to HDTV (1920x1080) progressive or interlaced. It uses
wavelets, motion compensation and arithmetic coding.

This package contains libraries for dirac.

%description libs -l pl.UTF-8
Dirac jest kodekiem ogólnego przeznaczenia dla obrazu o
rozdzielczościach od QCIF (180x144) do HDTV (1920x1080). Kodek ten
wykorzystuje fale elementarne (wavelets), kompensację ruchu (motion
compensation) oraz kodowanie arytmetyczne (arithmetic coding).

Ten pakiet zawiera biblioteki kodeka dirac.

%package devel
Summary:	Header files for dirac library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dirac
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for dirac library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dirac.

%package static
Summary:	Static dirac library
Summary(pl.UTF-8):	Statyczna biblioteka dirac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dirac library.

%description static -l pl.UTF-8
Statyczna biblioteka dirac.

%package apidocs
Summary:	dirac API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki dirac
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for dirac library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki dirac.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CPPUNITTESTS_DIR=

rm -f doc/api/html/*.md5
rm -rf $RPM_BUILD_ROOT%{_docdir}/dirac

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/BMPtoRGB
%attr(755,root,root) %{_bindir}/RGBtoBMP
%attr(755,root,root) %{_bindir}/RGBtoUYVY
%attr(755,root,root) %{_bindir}/RGBtoYUV411
%attr(755,root,root) %{_bindir}/RGBtoYUV420
%attr(755,root,root) %{_bindir}/RGBtoYUV422
%attr(755,root,root) %{_bindir}/RGBtoYUV444
%attr(755,root,root) %{_bindir}/UYVYtoRGB
%attr(755,root,root) %{_bindir}/UYVYtoYUV422
%attr(755,root,root) %{_bindir}/YUV411toRGB
%attr(755,root,root) %{_bindir}/YUV420Down2x2
%attr(755,root,root) %{_bindir}/YUV420ItoYUV422I
%attr(755,root,root) %{_bindir}/YUV420pt75filter
%attr(755,root,root) %{_bindir}/YUV420toRGB
%attr(755,root,root) %{_bindir}/YUV420toYUV422
%attr(755,root,root) %{_bindir}/YUV422ItoYUV420I
%attr(755,root,root) %{_bindir}/YUV422toRGB
%attr(755,root,root) %{_bindir}/YUV422toUYVY
%attr(755,root,root) %{_bindir}/YUV422toYUV420
%attr(755,root,root) %{_bindir}/YUV444toRGB
%attr(755,root,root) %{_bindir}/create_dirac_testfile.pl
%attr(755,root,root) %{_bindir}/dirac_decoder
%attr(755,root,root) %{_bindir}/dirac_encoder
%attr(755,root,root) %{_bindir}/dirac_instrumentation

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdirac_decoder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirac_decoder.so.0
%attr(755,root,root) %{_libdir}/libdirac_encoder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirac_encoder.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdirac_decoder.so
%attr(755,root,root) %{_libdir}/libdirac_encoder.so
%{_libdir}/libdirac_decoder.la
%{_libdir}/libdirac_encoder.la
%{_includedir}/%{name}
%{_pkgconfigdir}/dirac.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdirac_decoder.a
%{_libdir}/libdirac_encoder.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html
%doc doc/dirac_api_{foot,head}.html
%endif
