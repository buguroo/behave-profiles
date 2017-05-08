from functools import lru_cache as _lru_cache
import os


@_lru_cache()
def _get_profiles_path(features_path):
    profiles_path = os.path.join(features_path, "profiles")

    if not os.path.isdir(profiles_path):
        raise RuntimeError("profiles directory is missing")
    else:
        return profiles_path


def the_profile(context, profile, encoding='utf-8'):
    profiles_path = _get_profiles_path(context._config.base_dir)
    filename = os.path.join(profiles_path, profile + '.profile')
    try:
        with open(filename, 'r', encoding=encoding) as profile_file:
            profile_steps = profile_file.read()
    except Exception as exc:
        raise RuntimeError("error reading profile") from exc
    else:
        context.execute_steps(profile_steps)


def the_following_profiles(context, encoding='utf-8'):
    if not context.table.ensure_column_exists("profile"):
        raise RuntimeError("profile column is mandatory")
    else:
        for row in context.table:
            the_profile(context, row["profile"], encoding)
