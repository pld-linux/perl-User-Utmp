%include	/usr/lib/rpm/macros.perl
%define		pdir	User
%define		pnam	Utmp
Summary:	User::Utmp Perl module
Summary(cs):	Modul User::Utmp pro Perl
Summary(da):	Perlmodul User::Utmp
Summary(de):	User::Utmp Perl Modul
Summary(es):	Módulo de Perl User::Utmp
Summary(fr):	Module Perl User::Utmp
Summary(it):	Modulo di Perl User::Utmp
Summary(ja):	User::Utmp Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	User::Utmp ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul User::Utmp
Summary(pl):	Modu³ Perla User::Utmp
Summary(pt):	Módulo de Perl User::Utmp
Summary(pt_BR):	Módulo Perl User::Utmp
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl User::Utmp
Summary(sv):	User::Utmp Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl User::Utmp
Summary(zh_CN):	User::Utmp Perl Ä£¿é
Name:		perl-User-Utmp
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
Patch1:		%{name}-strcmp-fix.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User::Utmp - Perl access to utmp-style databases.

%description -l pl
User::Utmp - umo¿liwia dostêp do baz danych w stylu utmp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -f example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/User
%{perl_sitearch}/User/Utmp.pm
%dir %{perl_sitearch}/auto/User
%dir %{perl_sitearch}/auto/User/Utmp
%{perl_sitearch}/auto/User/Utmp/Utmp.bs
%attr(755,root,root) %{perl_sitearch}/auto/User/Utmp/Utmp.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
