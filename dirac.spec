Summary:	General purpose video codec
Summary(pl.UTF-8):	Kodek obrazu ogólnego przeznaczenia
Name:		dirac
Version:	1.0.0
Release:	2
License:	MPL v1.1 or GPL v2 or LGPL v2.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/dirac/%{name}-%{version}.tar.gz
# Source0-md5:	017b8d7d54caf9400ef72dcaee34a9d6
Patch0:		%{name}-am.patch
URL:		http://www.bbc.co.uk/rd/projects/dirac/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	perl-base
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-latex
BuildRequires:	tetex-metafont
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

%package devel
Summary:	Header files for dirac library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dirac
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
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

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	CPPUNITTESTS_DIR=

rm -f doc/api/html/*.md5
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/dirac

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libdirac_decoder.so.*.*.*
%attr(755,root,root) %{_libdir}/libdirac_encoder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdirac_decoder.so.0
%attr(755,root,root) %ghost %{_libdir}/libdirac_encoder.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html
%doc doc/dirac_api_{foot,head}.html
%attr(755,root,root) %{_libdir}/libdirac_decoder.so
%attr(755,root,root) %{_libdir}/libdirac_encoder.so
%{_libdir}/libdirac_decoder.la
%{_libdir}/libdirac_encoder.la
%{_includedir}/%{name}
%{_pkgconfigdir}/dirac.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libdirac_decoder.a
%{_libdir}/libdirac_encoder.a
