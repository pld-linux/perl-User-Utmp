#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	User
%define	pnam	Utmp
Summary:	User::Utmp Perl module
Summary(cs):	Modul User::Utmp pro Perl
Summary(da):	Perlmodul User::Utmp
Summary(de):	User::Utmp Perl Modul
Summary(es):	Módulo de Perl User::Utmp
Summary(fr):	Module Perl User::Utmp
Summary(it):	Modulo di Perl User::Utmp
Summary(ja):	User::Utmp Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	User::Utmp ÆÞ ¸ðÁÙ
Summary(nb):	Perlmodul User::Utmp
Summary(pl):	Modu³ Perla User::Utmp
Summary(pt):	Módulo de Perl User::Utmp
Summary(pt_BR):	Módulo Perl User::Utmp
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl User::Utmp
Summary(sv):	User::Utmp Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl User::Utmp
Summary(zh_CN):	User::Utmp Perl Ä£¿é
Name:		perl-User-Utmp
Version:	1.01
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dc2e12a78cc32d46e508577d26c9acce
Patch0:		%{name}-paths.patch
Patch1:		%{name}-strcmp-fix.patch
Patch2:		%{name}-doc.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The User::Utmp Perl module provides a simple Perl interface to utmp-
and utmpx-style databases on UNIX systems, the most important being
/var/run/utmp, which provides information about users currently
logged in. There is also experimental support for writing utmp files.

%description -l pl
Modu³ Perla User::Utmp udostêpnia prosty interfejs w Perlu to plików
baz danych typu utmp i utmpx w systemach UNIX. Najwa¿niejszym z nich
jest /var/run/utmp, który udostêpnia informacje o aktualnie
zalogowanych u¿ytkownikach. Jest równie¿ eksperymentalne wsparcie dla
zapisu do plików utmp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
