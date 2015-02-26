#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	User
%define		pnam	Utmp
Summary:	User::Utmp - Perl access to utmp- and utmpx-style databases
Summary(pl.UTF-8):	User::Utmp - dostęp z poziomu Perla do baz typu utmp i utmpx
Name:		perl-User-Utmp
Version:	1.8
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/User/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3561ae2b07f08b0c754bc351e810551
Patch0:		%{name}-strcmp-fix.patch
URL:		http://search.cpan.org/dist/User-Utmp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The User::Utmp Perl module provides a simple Perl interface to utmp-
and utmpx-style databases on UNIX systems, the most important being
/var/run/utmp, which provides information about users currently
logged in. There is also experimental support for writing utmp files.

%description -l pl.UTF-8
Moduł Perla User::Utmp udostępnia prosty interfejs w Perlu to plików
baz danych typu utmp i utmpx w systemach UNIX. Najważniejszym z nich
jest /var/run/utmp, który udostępnia informacje o aktualnie
zalogowanych użytkownikach. Jest również eksperymentalne wsparcie dla
zapisu do plików utmp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv -f $RPM_BUILD_ROOT%{perl_vendorarch}/User/example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/User
%{perl_vendorarch}/User/Utmp.pm
%dir %{perl_vendorarch}/auto/User
%dir %{perl_vendorarch}/auto/User/Utmp
%{perl_vendorarch}/auto/User/Utmp/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/User/Utmp/Utmp.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
