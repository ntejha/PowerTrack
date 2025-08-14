# Mamba Quick Guide

## Install Mamba
```bash
conda install -n base -c conda-forge mamba
````

## Create Environment

```bash
mamba create -n <env_name> python=3.11
mamba activate <env_name>
```

## Create from `environment.yml`

```bash
mamba env create -f environment.yml
```

## Export Environment

```bash
mamba env export --no-builds > environment.yml
```

## Update Environment

```bash
mamba env update -f environment.yml --prune
```

## Install Packages

```bash
mamba install <package>
mamba install -c conda-forge <package>
```

## Update Packages

```bash
mamba update <package>
mamba update --all
```

## Remove Package / Environment

```bash
mamba remove <package>
mamba env remove -n <env_name>
```

---
