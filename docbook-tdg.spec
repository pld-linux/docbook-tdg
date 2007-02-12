Summary:	DocBook The Definitive Guide
Summary(pl.UTF-8):   Rozstrzygający przewodnik (The Definitive Guide) po DocBooku
Name:		docbook-tdg
Version:	2.0.15
Release:	1
License:	FDL
Group:		Applications/Text
Source0:	http://www.docbook.org/tdg/en/tdg-en-html-%{version}.zip
# Source0-md5:	fdce21a3fdcf1d350789cbf847c7bf4a
URL:		http://www.docbook.org/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains "DocBook: The Definitive Guide". The definitive
guide, written by Norman Walsh and Leonard Muellner and published by
O'Reilly & Associates, Inc., is the official documentation for
DocBook.

%description -l pl.UTF-8
Ten pakiet zawiera publikację "DocBook: The Definitive Guide"
(Rozstrzygający przewodnik po DocBooku). Podręcznik został napisany
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
