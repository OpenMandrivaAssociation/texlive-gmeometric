Name:		texlive-gmeometric
Version:	0.73
Release:	1
Summary:	Change page size wherever it's safe
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmeometric
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmeometric.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmeometric.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Changing the size of the typeset area is well-known to be a
dangerous operation in TeX documents. This package identifies
the circumstances where the \geometry command of the geometry
package may safely be used, (other, of course, than in the
preamble of a document) and provides a mechanism for using it.
The package makes use of the author's gmutils package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmeometric/gmeometric.sty
%doc %{_texmfdistdir}/doc/latex/gmeometric/README
%doc %{_texmfdistdir}/doc/latex/gmeometric/gmeometric.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
