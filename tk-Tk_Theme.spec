Summary:	Tk_Theme
Name:		tk-Tk_Theme
Version:	23
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://www.xmission.com/~georgeps/Tk_Theme/Tk_Theme-%{version}.tgz
# Source0-md5:	121c335e3b3764cbd04eea68b6a66dd3
URL:		http://www.xmission.com/~georgeps/Tk_Theme/
Requires:	tk >= 8.4.3
BuildRequires:	tk-devel >= 8.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk_Theme

%prep
%setup -q -n Tk_Theme-%{version}

%build
tclsh configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/Tk_Theme-%{version}

sed -i -e 's#/usr/local/bin/wish.*#%{_bindir}/wish#g' *.tcl
install *.so *.tcl *.xpm *.gif $RPM_BUILD_ROOT%{_libdir}/Tk_Theme-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%dir %{_libdir}/Tk_Theme-*
%attr(755,root,root) %{_libdir}/Tk_Theme-*/*.so
%{_libdir}/Tk_Theme-*/*.tcl
%{_libdir}/Tk_Theme-*/*.gif
%{_libdir}/Tk_Theme-*/*.xpm
