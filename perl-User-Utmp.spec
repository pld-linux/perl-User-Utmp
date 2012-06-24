#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	User
%define		pnam	Utmp
Summary:	User::Utmp Perl module
Summary(cs):	Modul User::Utmp pro Perl
Summary(da):	Perlmodul User::Utmp
Summary(de):	User::Utmp Perl Modul
Summary(es):	M�dulo de Perl User::Utmp
Summary(fr):	Module Perl User::Utmp
Summary(it):	Modulo di Perl User::Utmp
Summary(ja):	User::Utmp Perl �⥸�塼��
Summary(ko):	User::Utmp �� ����
Summary(no):	Perlmodul User::Utmp
Summary(pl):	Modu� Perla User::Utmp
Summary(pt):	M�dulo de Perl User::Utmp
Summary(pt_BR):	M�dulo Perl User::Utmp
Summary(ru):	������ ��� Perl User::Utmp
Summary(sv):	User::Utmp Perlmodul
Summary(uk):	������ ��� Perl User::Utmp
Summary(zh_CN):	User::Utmp Perl ģ��
Name:		perl-User-Utmp
Version:	1.01
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-strcmp-fix.patch
Patch2:		%{name}-doc.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The User::Utmp Perl module provides a simple Perl interface to utmp-
and utmpx-style databases on UNIX systems, the most important being
/var/run/utmp, which provides information about users currently
logged in. There is also experimental support for writing utmp files.

%description -l pl
Modu� Perla User::Utmp udost�pnia prosty interfejs w Perlu to plik�w
baz danych typu utmp i utmpx w systemach UNIX. Najwa�niejszym z nich
jest /var/run/utmp, kt�ry udost�pnia informacje o aktualnie
zalogowanych u�ytkownikach. Jest r�wnie� eksperymentalne wsparcie dla
zapisu do plik�w utmp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{perl_sitearch}/User/example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/User
%{perl_sitearch}/User/Utmp.pm
%dir %{perl_sitearch}/auto/User
%dir %{perl_sitearch}/auto/User/Utmp
%{perl_sitearch}/auto/User/Utmp/autosplit.ix
%{perl_sitearch}/auto/User/Utmp/Utmp.bs
%attr(755,root,root) %{perl_sitearch}/auto/User/Utmp/Utmp.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
