Name:		python-mixpanel
Version:	4.10.1
Release:	1
Summary:	Official Mixpanel Python library
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/mixpanel/mixpanel-python
Source0:	https://files.pythonhosted.org/packages/source/m/mixpanel/mixpanel-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(six)

%description
Mixpanel analytics client. Aider uses it for optional telemetry.
4.10.1 is packaged instead of 5.x because 5.4.0 requires
unpackaged json-logic 0.7.0a0.

%files
%doc README.rst
%license LICENSE.txt
%{py_sitedir}/mixpanel.py
%{py_sitedir}/__pycache__/mixpanel*
%{py_sitedir}/mixpanel-*.*-info
