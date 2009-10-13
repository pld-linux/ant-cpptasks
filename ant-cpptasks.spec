
%if "%{pld_release}" == "ti"
%bcond_without	java_sun	# build with gcj
%else
%bcond_with	java_sun	# build with java-sun
%endif
#
%include	/usr/lib/rpm/macros.java

%define		_rc	b5

Summary:	C/C++, FORTRAN, MIDL and Windows Resource compilers tasks for ant
Name:		ant-cpptasks
Version:	1.0
Release:	0.%{_rc}.1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0: http://downloads.sourceforge.net/project/ant-contrib/ant-contrib/cpptasks-1.0-beta5/cpptasks-1.0%{_rc}.tar.gz
# Source0-md5:	7f0f7732acd0c82f7efb228f667ec79a
URL:		http://sf.net/projects/ant-contrib
BuildRequires:	ant
%{!?with_java_sun:BuildRequires:	java-gcj-compat-devel}
%{?with_java_sun:BuildRequires:	java-sun}
BuildRequires:	java-xerces
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
# for %{_javadir}
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cc task can compile various source languages and produce executables,
shared libraries (aka DLL's) and static libraries. Compiler adaptors are
currently available for C/C++, FORTRAN, MIDL and Windows Resource compilers.

%prep
%setup -q -n cpptasks-%{version}%{_rc}

%build
export JAVA_HOME="%{java_home}"

required_jars="xerces-j2"
CLASSPATH=$(build-classpath $required_jars)

%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}/ant

# jars
cp -a target/lib/cpptasks.jar $RPM_BUILD_ROOT%{_javadir}/ant/cpptasks.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/ant/*.jar
