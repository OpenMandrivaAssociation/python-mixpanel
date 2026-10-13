Name:		python-mixpanel
Version:	4.10.1
Release:	2
Summary:	Official Mixpanel Python library
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/mixpanel/mixpanel-python
Source0:	https://files.pythonhosted.org/packages/source/m/mixpanel/mixpanel-%{version}.tar.gz
BuildArch:	noarch
# METADATA floors would fail extra tests if cooker versions differ
%global __requires_exclude ^python[0-9.]*dist\\(
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(requests)
Requires:	python%{pyver}dist(six)
Requires:	python%{pyver}dist(urllib3)

%description
Mixpanel analytics client. Aider uses it for optional telemetry.
4.10.1 is packaged instead of 5.x because 5.4.0 requires
unpackaged json-logic 0.7.0a0.

%files
%doc README.rst
%license LICENSE.txt
%{py_sitedir}/mixpanel
%{py_sitedir}/mixpanel-*.*-info
