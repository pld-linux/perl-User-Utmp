%include	/usr/lib/rpm/macros.perl
Summary:	User-Utmp perl module
Summary(pl):	Modu³ perla User-Utmp
Name:		perl-User-Utmp
Version:	0.02
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/User/User-Utmp-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User-Utmp - Perl access to utmp-style databases.

%description -l pl
User-Utmp - umo¿liwia dostêp do baz danych w stylu utmp.

%prep
%setup -q -n User-Utmp-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz example.pl
%{perl_sitearch}/User/Utmp.pm
%dir %{perl_sitearch}/auto/User/Utmp
%{perl_sitearch}/auto/User/Utmp/autosplit.ix
%{perl_sitearch}/auto/User/Utmp/Utmp.bs
%attr(755,root,root) %{perl_sitearch}/auto/User/Utmp/Utmp.so
%{_mandir}/man3/*
