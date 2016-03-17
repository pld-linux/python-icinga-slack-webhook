%define		module	icinga-slack-webhook
Summary:	icinga_slack.webhook: A notifier from Icinga/Nagios to Slack
Name:		python-%{module}
Version:	1.0.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/i/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	c80ea1562166c7847f355a2791a6e7c0
URL:		https://github.com/samjsharpe/icinga_slack_webhook
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A script to send notifications to Slack.com from Nagios or Icinga via
the generic webhook integration

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/icinga_slack_webhook_notify
%{py_sitescriptdir}/icinga_slack
%{py_sitescriptdir}/icinga_slack_webhook-%{version}-py*.egg-info
