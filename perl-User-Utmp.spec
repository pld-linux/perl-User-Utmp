%include	/usr/lib/rpm/macros.perl
Summary:	User-Utmp perl module
Summary(pl):	Modu³ perla User-Utmp
Name:		perl-User-Utmp
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/User/User-Utmp-%{version}.tar.gz
Patch:		perl-User-Utmp-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/User/Utmp/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/User/Utmp
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz example.pl

%{perl_sitearch}/User/Utmp.pm

%dir %{perl_sitearch}/auto/User/Utmp
%{perl_sitearch}/auto/User/Utmp/.packlist
%{perl_sitearch}/auto/User/Utmp/autosplit.ix
%{perl_sitearch}/auto/User/Utmp/Utmp.bs
%attr(755,root,root) %{perl_sitearch}/auto/User/Utmp/Utmp.so

%{_mandir}/man3/*
