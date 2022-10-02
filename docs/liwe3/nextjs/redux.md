# Redux


## Custom Redux Functions

It is possible to add custom Redux functions, in addition to the ones already provided by every module.
To create one or more custom functions, you must modify the `initial_state.ts` file inside the module you want to add the functions to.

### Custom function creation

Here there is an example for the `user` module:

```typescript title="Creating a custom user_hello redux function" linenums="1"
/*=== d2r_start _import ===*/
import { User, UserFaceRec } from './core/types';

import { ReduxFunctions } from './reducer_functions'; // (1)

ReduxFunctions.user_hello = ( new_state: UserState, user: User ) => {  // (2)
	console.log( "==== USER HELLO" );
	return new_state;  // (3)
};
/*=== d2r_end _import ===*/
```

1. First of all, import `ReduxFunctions` from the `reducer_functions` file of the module you want to add the action to.

2. Simply add a new function to the `ReduxFunctions` object, with the name of the action you want to create.

3. Please keep in mind that the function must return the new state, even if it is not modified. As any standard reducer function does.


As you can see, the first thing you need to do is to import the `ReduxFunctions` object from the `reducer_functions` file of the module you want to add the action to (line 4).

Then, you can simply add a new function to the `ReduxFunctions` object, with the name of the function reducer you want to create (line 6 and onwards).

Since the function is a reducer, it must return the new state, even if it is not modified, you can simply return the `new_state` parameter.

!!! warning

    The file `initial_state.ts` is automatically generated, so, as usual, remember to make your modifications inside the `=== d2r_start ===` and `=== d2r_end ===` tags.

### Invoking a custom function

To invoke a custom function, you can use the `dispatch` function, as you would do with any other Redux function.

The `type` parameter of the `dispatch` function must be the name of the custom function you want to invoke.

``` typescript title="Invoking a custom user_hello redux function" linenums="1"
dispatch( {
	type: 'user_hello', // (1)
	payload: { user: null } // (2)
} );
```

1. The `type` parameter of the `dispatch` function must be the name of the custom function you want to invoke.

2. The payload can be any object you want.