#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	version
Summary:	version - Perl extension for Version Objects
#Summary(pl):	
Name:		perl-version
Version:	0.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JP/JPEACOCK/%{pdir}-%{version}.tar.gz
# Source0-md5:	f2e97a7d82d5351d97854106be9f9c4c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.45
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Overloaded version objects for all versions of Perl.  This module
implements all of the features of version objects which will be part
of Perl 5.10.0 except automatic version object creation.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/version/
%{perl_vendorarch}/auto/version//*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/version//*.so
%{_mandir}/man3/*
