%include	/usr/lib/rpm/macros.perl
Summary:	CGI-LogCarp perl module
Summary(pl):	Modu³ perla CGI-LogCarp
Name:		perl-CGI-LogCarp
Version:	1.12
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/LogCarp-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-LogCarp redefines the STDERR stream and allows the definition of
new STDBUG and STDLOG streams in such a way that all messages are
formatted similar to an HTTPD error log.

%description -l pl
CGI-LogCarp redefiniuje strumieñ STDERR i umo¿liwia zdefiniowanie
nowych strumieni STDEBUG i STDLOG w taki sposób, ¿eby wszystkie
informacje by³y formatowane w podobnym stylu jak logi serwera httpd.

%prep
%setup -q -n LogCarp-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/LogCarp
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,TODO}.gz

%{perl_sitelib}/CGI/LogCarp.pm
%{perl_sitearch}/auto/CGI/LogCarp

%{_mandir}/man3/*
