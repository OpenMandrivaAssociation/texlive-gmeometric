# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gmeometric
# catalog-date 2008-11-23 19:39:24 +0100
# catalog-license lppl
# catalog-version 0.73
Name:		texlive-gmeometric
Version:	0.73
Release:	6
Summary:	Change page size wherever it's safe
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmeometric
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmeometric.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmeometric.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Changing the size of the typeset area is well-known to be a
dangerous operation in TeX documents. This package identifies
the circumstances where the \geometry command of the geometry
package may safely be used, (other, of course, than in the
preamble of a document) and provides a mechanism for using it.
The package makes use of the author's gmutils package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.73-2
+ Revision: 752359
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.73-1
+ Revision: 718564
- texlive-gmeometric
- texlive-gmeometric
- texlive-gmeometric
- texlive-gmeometric

