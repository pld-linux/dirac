Summary:	General purpose video codec
Summary(pl):	Kodek obrazu ogólnego przeznaczenia
Name:		dirac
Version:	0.4.3
Release:	1
License:	Mozilla Public License
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b28f85349c09e6f82076f1cd0f75df3e
Patch0:		%{name}-shared.patch
URL:		http://www.bbc.co.uk/rd/projects/dirac/
BuildRequires:	autoconf
BuildRequires:	automake
Buildrequires:	doxygen
BuildRequires:	libtool
BuildRequires:	perl-base
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
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__perl} -pi -e 's@libdirac_common/@@g' \
	$RPM_BUILD_ROOT%{_includedir}/%{name}/*.h
%{__perl} -pi -e 's@libdirac_motionest/@@g' \
	$RPM_BUILD_ROOT%{_includedir}/%{name}/*.h

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
