<a id="startup-startup-kernel"></a>
## `startup_kernel`


```ts
startup_kernel = async (): Promise<ILiWE>
```


Bootstraps the whole LiWE Framework
This is the "kernel" version since it only creates the basic settings.
This method is useful in tests to bootstrap a working environment.






**Returns**: `an object with all basic components inited`

-----------------

<a id="startup-startup"></a>
## `startup`


```ts
startup = async ( options: LiWEServerOptions = } ): Promise<ILiWE>
```


This is the main function that startups the whole LiWE Framework






**Returns**: `an initialized ILiWE structure`

-----------------

