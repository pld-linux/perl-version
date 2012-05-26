#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	version
Summary:	version - Perl extension for Version Objects
Summary(pl.UTF-8):	version - rozszerzenie Perla dla obiektów wersji
Name:		perl-version
Version:	0.99
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/version/%{pdir}-%{version}.tar.gz
# Source0-md5:	695098dac5c3be79e893e522341671dd
URL:		http://search.cpan.org/dist/version/
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Temp >= 0.13
BuildRequires:	perl-Test-Simple >= 0.45
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Overloaded version objects for all versions of Perl. This module
implements all of the features of version objects which will be part
of Perl 5.10.0 except automatic version object creation.

%description -l pl.UTF-8
Przeciążone obiekty wersji dla wszystkich wersji Perla. Ten moduł
implementuje wszystkie możliwości obiektów wersji, które będą częścią
Perla 5.10.0, z wyjątkiem automatycznego tworzenia obiektu wersji.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/version/Internals.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/version.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/version.pm
%dir %{perl_vendorarch}/version
%{perl_vendorarch}/version/vxs.pm
%dir %{perl_vendorarch}/auto/version
%dir %{perl_vendorarch}/auto/version/vxs
%attr(755,root,root) %{perl_vendorarch}/auto/version/vxs/vxs.so
%{perl_vendorarch}/auto/version/vxs/vxs.bs
%{_mandir}/man3/version*.3pm*
