#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# "i'm dumb therefore i fail"
#
%include	/usr/lib/rpm/macros.perl
Summary:	CGI::LogCarp perl module
Summary(pl):	Modu� perla CGI::LogCarp
Name:		perl-CGI-LogCarp
Version:	1.12
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/LogCarp-%{version}.tar.gz
# Source0-md5:	850d4b10812339a95fd4b21680a4c692
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::LogCarp redefines the STDERR stream and allows the definition of
new STDBUG and STDLOG streams in such a way that all messages are
formatted similar to an HTTPD error log.

%description -l pl
CGI::LogCarp redefiniuje strumie� STDERR i umo�liwia zdefiniowanie
nowych strumieni STDEBUG i STDLOG w taki spos�b, �eby wszystkie
informacje by�y formatowane w podobnym stylu jak logi serwera httpd.

%prep
%setup -q -n LogCarp-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/CGI/LogCarp.pm
%{_mandir}/man3/*
