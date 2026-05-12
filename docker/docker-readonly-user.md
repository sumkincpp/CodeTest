# Docker UID/GID Hardcoded Value - Recommendation

**Use `10000:10001`**

- Above all system ranges (`0–999`) on every Linux distro — no host collision possible
- Asymmetric UID/GID makes ownership unambiguous in `ls -la`
- `chown 10000:10001` works universally across hosts
- Source: [hexops/dockerfile](https://github.com/hexops-graveyard/dockerfile) (Sourcegraph production guide)

```dockerfile
RUN groupadd --gid 10001 appgroup \
 && useradd --uid 10000 --gid 10001 --no-create-home --shell /sbin/nologin appuser
USER 10000:10001
```

## Who Uses What

| Value | Used by | Notes |
|---|---|---|
| `10000:10001` | Sourcegraph, hexops guide | General app containers |
| `65532:65532` | Google Distroless, Tekton (CNCF), Chainguard | Distroless/scratch base images only |
| `65534:65534` | Linux kernel `nobody`, Alpine | No `useradd` needed; shared identity — not app-specific |
| `101:101` | Official nginx image | Legacy service convention; in system range, avoid for new apps |
| `999:999` | Redis, many older official images | Collides with RHEL/Fedora system accounts (`systemd-coredump`) |

## Hard Rules

- Never below `1000` - system range (LSB spec, Red Hat, Debian, systemd)
- Never `65534` for app user - that is `nobody`, a shared kernel identity
- Never `999` or below for services - collides with distro-managed accounts ([valkey-io/valkey-container#33](https://github.com/valkey-io/valkey-container/issues/33))

## References

- [Sourcegraph / hexops Dockerfile best practices](https://github.com/hexops-graveyard/dockerfile)
- [Google Distroless nonroot UID 65532 documentation](https://github.com/GoogleContainerTools/distroless/issues/443)
- [Tekton fix: distroless nonroot is 65532 not 1001](https://github.com/tektoncd/pipeline/pull/3342)
- [Valkey container issue: UID 999 collides with RHEL system accounts](https://github.com/valkey-io/valkey-container/issues/33)
- [systemd UIDS-GIDS.md — UID range definitions](https://systemd.io/UIDS-GIDS/)
- [Linux Standard Base — UID ranges (Baeldung)](https://www.baeldung.com/linux/user-ids-reserved-values)
- [Docker official blog — USER instruction best practices](https://www.docker.com/blog/understanding-the-docker-user-instruction/)
- [Official nginx image — uid=101](https://hub.docker.com/_/nginx)
- [CIS Docker Benchmark v1.7 — section 4.1 non-root user](https://www.cisecurity.org/benchmark/docker) - no specific recommendation
