Summary:	General purpose video codec
Summary(pl):	Kodek obrazu ogólnego przeznaczenia
Name:		dirac
Version:	0.5.0
Release:	1
License:	MPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/dirac/%{name}-%{version}.tar.gz
# Source0-md5:	5874a2d2cdb74d3356483b1c47bb941e
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.map

%description
Dirac is a general-purpose video codec aimed at resolutions from QCIF
(180x144) to HDTV (1920x1080) progressive or interlaced. It uses
wavelets, motion compensation and arithmetic coding.

%description -l pl
Dirac jest kodekiem ogólnego przeznaczenia dla obrazu o
rozdzielczo¶ciach od QCIF (180x144) do HDTV (1920x1080). Kodek ten
wykorzystuje fale elementarne (wavelets), kompensacjê ruchu (motion
compensation) oraz kodowanie arytmetyczne (arithmetic coding).

%package devel
Summary:	Header files for dirac library
Summary(pl):	Pliki nag³ówkowe biblioteki dirac
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for dirac library.

%description devel -l pl
Pliki nag³ówkowe biblioteki dirac.

%package static
Summary:	Static dirac library
Summary(pl):	Statyczna biblioteka dirac
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static dirac library.

%description static -l pl
Statyczna biblioteka dirac.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/api/{Makefile*,dirac_api.doxygen,dirac_api_foot.html,dirac_api_head.html,html/{*.md5,graph_legend.dot}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/faq.htm
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/api doc/programmers/programmers_guide.pdf doc/dirac_doc_howto.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
