//go:build k8srequired
// +build k8srequired

package basic

import (
	"context"
	"fmt"
	"os"
	"testing"

	"github.com/giantswarm/apptest"
	"github.com/giantswarm/micrologger"

	"github.com/giantswarm/k8s-dns-node-cache-app/v2/integration/env"
	"github.com/giantswarm/k8s-dns-node-cache-app/v2/integration/templates"
)

const (
	app           = "k8s-dns-node-cache-test"
	appName       = "k8s-dns-node-cache-app"
	catalogName   = "giantswarm-test"
	testNamespace = "kube-system"
)

var (
	appTest apptest.Interface
	l       micrologger.Logger
)

func init() {
	var err error

	{
		c := micrologger.Config{}
		l, err = micrologger.New(c)
		if err != nil {
			panic(err.Error())
		}
	}

	{
		c := apptest.Config{
			Logger: l,

			KubeConfigPath: env.KubeConfig(),
		}
		appTest, err = apptest.New(c)
		if err != nil {
			panic(err.Error())
		}
	}
}

// TestMain allows us to have common setup and teardown steps that are run
// once for all the tests https://golang.org/pkg/testing/#hdr-Main.
func TestMain(m *testing.M) {
	ctx := context.Background()

	var err error

	{
		apps := []apptest.App{
			{
				CatalogName:   catalogName,
				Name:          appName,
				Namespace:     testNamespace,
				SHA:           env.CircleSHA(),
				ValuesYAML:    templates.K8sDnsNodeCacheValues,
				WaitForDeploy: true,
			},
		}
		err = appTest.InstallApps(ctx, apps)
		if err != nil {
			l.LogCtx(ctx, "level", "error", "message", "install apps failed", "stack", fmt.Sprintf("%#v\n", err))
			os.Exit(-1)
		}
	}

	os.Exit(m.Run())
}
