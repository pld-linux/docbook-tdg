Summary:	DocBook The Definitive Guide
Summary(pl):	Rozstrzygaj±cy przewodnik (The Definitive Guide) po DocBooku
Name:		docbook-tdg
Version:	2.0.9
Release:	0.Alpha.1
License:	FDL
Group:		Applications/Text
Source0:	http://www.docbook.org/tdg/en/tdg-en-html-%{version}.zip
# Source0-md5:	4de8c6cb42e891cf81955896f8c2c358
URL:		http://www.docbook.org/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains "DocBook: The Definitive Guide". The definitive
guide, written by Norman Walsh and Leonard Muellner and published by
O'Reilly & Associates, Inc., is the official documentation for
DocBook.

%description -l pl
Ten pakiet zawiera publikacjê "DocBook: The Definitive Guide"
(Rozstrzygaj±cy przewodnik po DocBooku). Podrêcznik zosta³ napisany
przez Normana Walsha oraz Leonarda Muellnera i wydany przez O'Reilly &
Associates, Inc. Jest to oficjalna dokumentacja dla DocBooka.

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
