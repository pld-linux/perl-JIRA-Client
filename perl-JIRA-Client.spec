#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	JIRA
%define		pnam	Client
%include	/usr/lib/rpm/macros.perl
Summary:	JIRA::Client - An extended interface to JIRA's SOAP API
Name:		perl-JIRA-Client
Version:	0.26
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GN/GNUSTAVO/modules/JIRA-Client-%{version}.tar.gz
# Source0-md5:	d44da752a7baeac1fdf43731ee6735d2
URL:		http://search.cpan.org/dist/JIRA-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-SOAP-Lite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JIRA is a proprietary bug tracking system from Atlassian
<http://www.atlassian.com/software/jira/>.

This module implements an Object Oriented wrapper around JIRA's SOAP
API

(This version is known to work with JIRA 4 but it was tested by the
author only against JIRA 3.13.4 so far.)

Moreover, it implements some other methods to make it easier to do
some common operations.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%dir %{perl_vendorlib}/JIRA
%{perl_vendorlib}/JIRA/Client.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
