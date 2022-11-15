Name:		texlive-cellprops
Version:	57599
Release:	1
Summary:	Accept CSS-like selectors in tabular, array, ...
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cellprops
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellprops.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellprops.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cellprops.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package reworks the internals of tabular, array, and
similar constructs, and adds a \cellprops command accepting
CSS-like selectors and properties. It depends on mdwtab,
xcolor, expl3, and xparse.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/cellprops
%{_texmfdistdir}/tex/latex/cellprops
%doc %{_texmfdistdir}/doc/latex/cellprops

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
