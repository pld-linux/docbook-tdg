Summary:	DocBook The Definitive Guide
Summary(pl):	Rozstrzygaj±cy przewodnik (The Definitive Guide) po DocBook
Name:		docbook-tdg
Version:	2.0.8
Release:	0.Alpha.1
License:	?
Group:		Applications/Text
Source0:	http://www.docbook.org/tdg/en/tdg-en-html-%{version}.zip
# Source0-md5:	cbf35fa7927bfe4850af6da26dac995e
URL:		http://www.docbook.org/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DocBook The Definitive Guide.

%description
Rozstrzygaj±cy przewodnik (The Definitive Guide) po DocBook.

%prep
%setup -q -n tdg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc en
