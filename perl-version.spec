#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	version
Summary:	version - Perl extension for Version Objects
Summary(pl.UTF-8):	version - rozszerzenie Perla dla obiektów wersji
Name:		perl-version
Version:	0.7702
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JP/JPEACOCK/%{pdir}-%{version}.tar.gz
# Source0-md5:	c1047db4f27fe3d740cf5552c12cb222
URL:		http://search.cpan.org/dist/version/
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.45
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/version/vxs/.packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/version.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README

%dir %{perl_vendorarch}/version
%dir %{perl_vendorarch}/auto/version
%dir %{perl_vendorarch}/auto/version/vxs

%attr(755,root,root)    %{perl_vendorarch}/auto/version/vxs/vxs.so
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/version/vxs/vxs.bs
%{perl_vendorarch}/version/vxs.pm

%{_mandir}/man3/*
