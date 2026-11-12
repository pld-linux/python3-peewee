#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	peewee
Summary:	A small, expressive ORM
Summary(pl.UTF-8):	Mały, ekspresyjny ORM
Name:		python3-%{module}
Version:	4.5.3
Release:	1
License:	MIT
Group:		Libraries/Python
# PyPI sdist lacks the test suite
#Source0Download: https://github.com/coleifer/peewee/tags
Source0:	https://github.com/coleifer/peewee/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	6f78ce01b7767a2967f0dabe72c485bb
URL:		https://docs.peewee-orm.com/
BuildRequires:	python3-Cython >= 3
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Peewee is a simple and small ORM. It has few (but expressive)
concepts, making it easy to learn and intuitive to use.

%description -l pl.UTF-8
Peewee to prosty i mały ORM. Ma niewiele (ale ekspresyjnych) koncepcji,
co czyni go łatwym do nauki i intuicyjnym w użyciu.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} runtests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/playhouse/_sqlite_udf.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE CHANGELOG.md README.rst
%attr(755,root,root) %{_bindir}/pwiz
%attr(755,root,root) %{_bindir}/pwmigrate
%{py3_sitedir}/peewee.py
%{py3_sitedir}/peewee-stubs
%{py3_sitedir}/playhouse
%{py3_sitedir}/pwiz.py
%{py3_sitedir}/__pycache__/peewee.cpython-*.py[co]
%{py3_sitedir}/__pycache__/pwiz.cpython-*.py[co]
%{py3_sitedir}/peewee-%{version}.dist-info
