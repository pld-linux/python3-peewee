#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	peewee
Summary:	A small, expressive ORM
Summary(pl.UTF-8):	Mały, ekspresyjny ORM
Name:		python3-%{module}
Version:	4.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/peewee/
Source0:	https://files.pythonhosted.org/packages/source/p/peewee/%{module}-%{version}.tar.gz
# Source0-md5:	544ba620be191bc24fd2fa343d5659d5
URL:		https://docs.peewee-orm.com/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
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
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE CHANGELOG.md README.rst
%attr(755,root,root) %{_bindir}/pwiz
%{py3_sitedir}/peewee.py
%{py3_sitedir}/playhouse
%{py3_sitedir}/pwiz.py
%{py3_sitedir}/__pycache__/peewee.cpython-*.py[co]
%{py3_sitedir}/__pycache__/pwiz.cpython-*.py[co]
%{py3_sitedir}/peewee-%{version}.dist-info
