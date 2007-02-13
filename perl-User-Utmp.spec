#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	User
%define		pnam	Utmp
Summary:	User::Utmp Perl module
Summary(cs.UTF-8):	Modul User::Utmp pro Perl
Summary(da.UTF-8):	Perlmodul User::Utmp
Summary(de.UTF-8):	User::Utmp Perl Modul
Summary(es.UTF-8):	Módulo de Perl User::Utmp
Summary(fr.UTF-8):	Module Perl User::Utmp
Summary(it.UTF-8):	Modulo di Perl User::Utmp
Summary(ja.UTF-8):	User::Utmp Perl モジュール
Summary(ko.UTF-8):	User::Utmp 펄 모줄
Summary(nb.UTF-8):	Perlmodul User::Utmp
Summary(pl.UTF-8):	Moduł Perla User::Utmp
Summary(pt.UTF-8):	Módulo de Perl User::Utmp
Summary(pt_BR.UTF-8):	Módulo Perl User::Utmp
Summary(ru.UTF-8):	Модуль для Perl User::Utmp
Summary(sv.UTF-8):	User::Utmp Perlmodul
Summary(uk.UTF-8):	Модуль для Perl User::Utmp
Summary(zh_CN.UTF-8):	User::Utmp Perl 模块
Name:		perl-User-Utmp
Version:	1.8
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3561ae2b07f08b0c754bc351e810551
Patch0:		%{name}-strcmp-fix.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
%{perl_vendorarch}/auto/User/Utmp/Utmp.bs
%attr(755,root,root) %{perl_vendorarch}/auto/User/Utmp/Utmp.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
