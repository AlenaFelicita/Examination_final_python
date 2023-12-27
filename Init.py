import subprocess


def site_is_not_vulnerable(site):
    result = subprocess.run(f'nikto -h {site} -ssl -Tuning 4', shell=True,
                            stdout=subprocess.PIPE, encoding='utf-8')
    return result.returncode == 0 and '0 error(s)' in result.stdout
