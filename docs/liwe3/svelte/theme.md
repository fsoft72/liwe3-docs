# LiWE3 Theme System

### Guide to the CSS Rules in `liwe3-styles.css`

#### Variables

The stylesheet defines several CSS variables to manage design consistency and theming.

##### Main Variables

These variables control the primary styles such as spacing, font properties, and breakpoints.

- **Spacing Variables**:

  ```css
  --liwe3-space-1: 0.25rem;
  --liwe3-space-2: 0.5rem;
  --liwe3-space-3: 1rem;
  --liwe3-space-4: 2rem;
  ```

- **Font Variables**:

  ```css
  --liwe3-main-font-family: Roboto, sans-serif;
  --liwe3-font-family: Roboto, sans-serif;
  --liwe3-secondary-font-family: Rozha One, serif;
  --liwe3-font-weight: 400;
  --liwe3-font-size: 20px;
  ```

- **Border Variables**:

  ```css
  --liwe3-border-radius: 0.15rem;
  --liwe3-border-width: 1px;
  --liwe3-border-style: solid;
  ```

- **Button Padding Variables**:

  ```css
  --liwe3-button-padding-y: 0.25rem;
  --liwe3-button-padding-x: 0.1rem;
  ```

- **Input Padding Variables**:

  ```css
  --liwe3-input-padding-y: 0.15rem;
  --liwe3-input-padding-x: 0.15rem;
  ```

- **Breakpoint Variables**:
  ```css
  --liwe3-breakpoint-xs: 0;
  --liwe3-breakpoint-sm: 640px;
  --liwe3-breakpoint-md: 768px;
  --liwe3-breakpoint-lg: 1024px;
  --liwe3-breakpoint-xl: 1280px;
  --liwe3-breakpoint-xxl: 1536px;
  --liwe3-breakpoint-4k: 1930px;
  ```

##### Appendix: Full List of Variables

```css
:root {
  --liwe3-main-font-family: Roboto, sans-serif;
  --liwe3-space-1: 0.25rem;
  --liwe3-space-2: 0.5rem;
  --liwe3-space-3: 1rem;
  --liwe3-space-4: 2rem;
  --liwe3-breakpoint-xs: 0;
  --liwe3-breakpoint-sm: 640px;
  --liwe3-breakpoint-md: 768px;
  --liwe3-breakpoint-lg: 1024px;
  --liwe3-breakpoint-xl: 1280px;
  --liwe3-breakpoint-xxl: 1536px;
  --liwe3-breakpoint-4k: 1930px;
  --liwe3-font-family: Roboto, sans-serif;
  --liwe3-secondary-font-family: Rozha One, serif;
  --liwe3-font-weight: 400;
  --liwe3-font-size: 20px;
  --liwe3-border-radius: 0.15rem;
  --liwe3-border-width: 1px;
  --liwe3-border-style: solid;
  --liwe3-button-padding-y: 0.25rem;
  --liwe3-button-padding-x: 0.1rem;
  --liwe3-input-padding-y: 0.15rem;
  --liwe3-input-padding-x: 0.15rem;
  --liwe3-form-checkbox-width: 26px;
}
```

#### Typography

Styles for text elements including headings, paragraphs, links, and other inline elements.

- **Headings**:

  ```css
  h1,
  h2 {
    font-family: var(--liwe3-secondary-font-family);
    font-weight: 700;
  }

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-weight: 700;
    margin: var(--liwe3-space-2) 0;
  }

  h1 {
    font-size: 2.5rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }

  h2 {
    font-size: 2rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }

  h3 {
    font-size: 1.75rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }

  h4 {
    font-size: 1.5rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }

  h5 {
    font-size: 1.25rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }

  h6 {
    font-size: 1rem;
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }
  ```

- **Paragraphs and Text**:

  ```css
  p,
  a,
  li,
  blockquote,
  small,
  code,
  pre,
  kbd,
  strong,
  input {
    font-size: 1rem;
    font-weight: var(--liwe3-font-weight);
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }
  ```

- **Links**:

  ```css
  a {
    color: var(--liwe3-link-color);
    text-decoration: none;
  }

  a:hover {
    color: var(--liwe3-link-hover-color);
    text-decoration: underline;
  }

  a:active {
    color: var(--liwe3-link-active-color);
  }
  ```

#### Layout

The stylesheet uses a grid system based on Flexbox to create responsive layouts.

- **Grid System**:
  The grid system is composed of rows and columns that adapt to different screen sizes using breakpoints.

  - **Grid Columns and Offsets**:

    ```css
    .liwe3-col-xs6 {
      flex: 0 0 calc((100 / 12) * 6%);
      max-width: calc((100 / 12) * 6%);
    }

    .liwe3-offset-xs6 {
      margin-left: calc((100 / 12) * 6%) !important;
    }
    ```

  - **Grid Column and Offset Classes for XS, SM, MD, LG Breakpoints**:

    ```css
    /* cols */
    .liwe3-col-xs1 {
      flex: 0 0 calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
      max-width: calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
    }

    .liwe3-col-sm1 {
      flex: 0 0 calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
      max-width: calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
    }

    .liwe3-col-md1 {
      flex: 0 0 calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
      max-width: calc((((100 - (0 * (12 - 1))) / 12) * 1) * 1%);
    }

    ...
    
    /* offset */
    
    .liwe3-offset-sm1 {
      margin-left: calc((100 / 12 * 1) * 1%) !important;
    }
    .liwe3-offset-md1 {
      margin-left: calc((100 / 12 * 1) * 1%) !important;
    }
    .liwe3-offset-xs1 {
      margin-left: calc((100 / 12 * 1) * 1%) !important;
    }
    ```

  - **Usage Example**:
    `html
    <div class="liwe3-container">
      <div class="liwe3-row">
        <div class="liwe3-col liwe3-col-xs6">Column 1</div>
        <div class="liwe3-col liwe3-col-xs6">Column 2</div>
      </div>
    </div>
    `
    **Layout and Flexbox Utilities**
    Flexbox utility classes to help with layout.

- **Flexbox Alignment**:

  ```css
  .liwe3-flex-start {
    justify-content: flex-start !important;
  }
  .liwe3-flex-end {
    justify-content: flex-end !important;
  }
  .liwe3-flex-center {
    justify-content: center !important;
  }
  .liwe3-flex-between {
    justify-content: space-between !important;
  }
  ```

- **Flexbox Alignment Along Cross Axis**:
  ```css
  .liwe3-flex-top {
    align-items: flex-start !important;
  }
  .liwe3-flex-bottom {
    align-items: flex-end !important;
  }
  .liwe3-flex-middle {
    align-items: center !important;
  }
  ```

#### Forms

Styles for form elements, including buttons, inputs, and checkboxes.

- **Button Styles**:

  ```css
  .liwe3-button {
    padding: var(--liwe3-button-padding-y) var(--liwe3-button-padding-x);
    border-width: var(--liwe3-border-width);
    border-style: var(--liwe3-border-style);
    border-color: var(--liwe3-button-border);
    border-radius: var(--liwe3-border-radius);
    background-color: var(--liwe3-button-background);
    font-size: var(--liwe3-font-size);
    user-select: none;
    cursor: pointer;
  }

  .liwe3-button:hover:not(:disabled) {
    background-color: var(--liwe3-button-hover);
  }

  .liwe3-button:disabled {
    cursor: default;
  }
  ```

  - **Usage**:
    ```html
    <button class="liwe3-button mode1">Primary Button</button>
    <button class="liwe3-button mode2">Secondary Button</button>
    <button class="liwe3-button mode3">Tertiary Button</button>
    <button class="liwe3-button mode4">Accent Button</button>
    ```

- **Input Fields**:

  ```css
  input {
    font-size: var(--liwe3-font-size);
    font-weight: var(--liwe3-font-weight);
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
    padding: var(--liwe3-input-padding-y) var(--liwe3-input-padding-x);
  }

  input::placeholder {
    font-size: 1rem;
    font-weight: var(--liwe3-font-weight);
    line-height: 1.2;
    letter-spacing: 0;
    text-align: left;
  }
  ```

  - **Usage**:
    ```html
    <input type="text" placeholder="Enter text" />
    <input type="email" placeholder="Enter email" />
    ```

- **Checkbox**:

  ```css
  .liwe3-form-checkbox {
    width: var(--liwe3-form-checkbox-width);
    height: var(--liwe3-form-checkbox-width);
  }
  ```

  - **Usage**:
    ```html
    <input type="checkbox" class="liwe3-form-checkbox" />
    ```
  - **Javascript generated color schemes variables**:
    ```css
    --liwe3-form-border-width-focus: calc(var(--liwe3-border-width) * 2);
    --liwe3-form-bg: var(--liwe3-[theme-variant]-mode3);
    --liwe3-form-text-color: var(--liwe3-[theme-variant]-mode3-500-text);
    --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4);
    --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-700);
    --liwe3-form-border-color: var(--liwe3-[theme-variant]-mode3-200-border);
    --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-mode3-500-hover);
    --liwe3-form-error: var(--liwe3-[theme-variant]-error-500);
    .mode1 {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-mode1);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-mode1-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-mode1-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-mode1-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-mode1-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-mode1-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode1);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode1-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-500-text);
      }
    }
    .mode2 {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-mode2);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-mode2-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-mode2-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-mode2-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-mode2-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-mode2-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode2);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode2-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-500-text);
      }
    }
    .mode3 {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-mode3);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-mode3-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-mode3-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-mode3-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-mode3-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-mode3-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode3);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode3-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-500-text);
      }
    }
    .mode4 {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-mode4);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-mode4-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-mode4-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-mode4-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-mode4-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-mode4-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-mode4-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-mode4-500-text);
      }
    }
    .link {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-link);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-link-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-link-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-link-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-link-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-link-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-link);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-link-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-link-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-link-500-text);
      }
    }
    .info {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-info);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-info-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-info-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-info-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-info-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-info-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-info);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-info-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-info-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-info-500-text);
      }
    }
    .success {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-success);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-success-500-text);
      --liwe3-form-border-color: var(
        --liwe3-[theme-variant]-success-200-border
      );
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-success-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-success-500-text
        ) !important;
        --liwe3-form-legend: var(--liwe3-[theme-variant]-success-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-success);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-success-500-text
        );
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-success-500-hover);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-success-500-text
        );
      }
    }
    .warning {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-warning);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-warning-500-text);
      --liwe3-form-border-color: var(
        --liwe3-[theme-variant]-warning-200-border
      );
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-warning-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-warning-500-text
        );
        --liwe3-form-legend: var(--liwe3-[theme-variant]-warning-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-warning);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-warning-500-text
        );
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-warning-500-hover);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-warning-500-text
        );
      }
    }
    .error {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-error);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-error-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-error-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-error-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-error-500-text
        );
        --liwe3-form-legend: var(--liwe3-[theme-variant]-error-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-error);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-error-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-error-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-error-500-text);
      }
    }
    .dark {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-background);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-background-500-text);
      --liwe3-form-border-color: var(
        --liwe3-[theme-variant]-background-200-border
      );
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-background-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
        --liwe3-form-legend: var(--liwe3-[theme-variant]-background-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-background);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-background-500-hover);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
      }
    }
    .background {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-background);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-background-500-text);
      --liwe3-form-border-color: var(
        --liwe3-[theme-variant]-background-200-border
      );
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-background-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
        --liwe3-form-legend: var(--liwe3-[theme-variant]-background-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-background);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-background-500-hover);
        --liwe3-form-accent-color: var(
          --liwe3-[theme-variant]-background-500-text
        );
      }
    }
    .color {
      --liwe3-form-bg: var(--liwe3-[theme-variant]-text);
      --liwe3-form-text-color: var(--liwe3-[theme-variant]-text-500-text);
      --liwe3-form-border-color: var(--liwe3-[theme-variant]-text-200-border);
      --liwe3-form-focus-bg: var(--liwe3-[theme-variant]-text-500-hover);
      &.liwe3-form-custom-input {
        --liwe3-form-text-placeholder-color: var(
          --liwe3-[theme-variant]-text-500-text
        );
        --liwe3-form-legend: var(--liwe3-[theme-variant]-text-200-border);
      }
      &.liwe3-form-custom-checkbox-radio {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-text);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-text-500-text);
      }
      &.liwe3-form-radio-group input[type="radio"]:checked + label {
        --liwe3-form-accent: var(--liwe3-[theme-variant]-text-500-hover);
        --liwe3-form-accent-color: var(--liwe3-[theme-variant]-text-500-text);
      }
    }
    .liwe3-form-custom-switch {
      --liwe3-form-text-placeholder-color: var(
        --liwe3-[theme-variant]-mode3-700-text
      );
      --liwe3-form-radius: var(--liwe3-border-radius);
    }
    .liwe3-form-custom-btn {
      --liwe3-form-btn-primary: var(--liwe3-[theme-variant]-mode3);
      --liwe3-form-btn-default-text: var(
        --liwe3-[theme-variant]-mode3-500-text
      );
      --liwe3-form-radius: var(--liwe3-border-radius);
    }
    .liwe3-form-radio-group {
      max-width: fit-content;
    }
    ```

- **Form and Layout Example**:
  ```html
  <div class="liwe3-container">
    <h1>Example Form</h1>
    <form>
      <div class="liwe3-row">
        <div class="liwe3-col liwe3-col-xs6">
          <label for="name">Name:</label>
          <input type="text" id="name" placeholder="Enter your name" />
        </div>
        <div class="liwe3-col liwe3-col-xs6">
          <label for="email">Email</label>
          <input type="email" id="email" placeholder="Enter your email" />
        </div>
      </div>
      <div class="liwe3-row">
        <div class="liwe3-col liwe3-col-xs6">
          <label for="subscribe">Subscribe:</label>
          <input type="checkbox" id="subscribe" class="liwe3-form-checkbox" />
        </div>
      </div>
      <div class="liwe3-row">
        <div class="liwe3-col liwe3-col-xs6">
          <button type="submit" class="liwe3-button mode1">Submit</button>
        </div>
        <div class="liwe3-col liwe3-col-xs6">
          <button type="reset" class="liwe3-button mode2">Reset</button>
        </div>
      </div>
    </form>
  </div>
  ```

#### Colors

The stylesheet defines a variety of color schemes for light and dark themes, including primary, secondary, tertiary, and accent colors. The colors are defined with shades ranging from 100 (lighter) to 900 (darker).

- **Light Theme Colors**:

  ```css
  .liwe3-light-theme {
    --liwe3-primary-color: var(--liwe3-light-mode1-500);
    --liwe3-lighter-primary-color: var(--liwe3-light-mode1-300);
    --liwe3-darker-primary-color: var(--liwe3-light-mode1-700);
    --liwe3-secondary-color: var(--liwe3-light-mode2-500);
    --liwe3-lighter-secondary-color: var(--liwe3-light-mode2-300);
    --liwe3-darker-secondary-color: var(--liwe3-light-mode2-700);
    --liwe3-tertiary-color: var(--liwe3-light-mode3-500);
    --liwe3-lighter-tertiary-color: var(--liwe3-light-mode3-300);
    --liwe3-darker-tertiary-color: var(--liwe3-light-mode3-700);
    --liwe3-accent-color: var(--liwe3-light-mode4-500);
    --liwe3-lighter-accent-color: var(--liwe3-light-mode4-300);
    --liwe3-darker-accent-color: var(--liwe3-light-mode4-700);
    --liwe3-background: var(--liwe3-light-background-color);
    --liwe3-color: var(--liwe3-light-text-color);
    --liwe3-link-color: var(--liwe3-light-link-color);
    --liwe3-link-hover-color: var(--liwe3-light-link-500-hover);
    --liwe3-link-active-color: var(--liwe3-light-link-500-active);
    --liwe3-link-visited-color: var(--liwe3-light-link-500-active);
    --liwe3-link-disabled-color: var(--liwe3-light-link-500-disabled);
    --liwe3-info-color: var(--liwe3-light-info);
    --liwe3-success-color: var(--liwe3-light-success);
    --liwe3-warning-color: var(--liwe3-light-warning);
    --liwe3-error-color: var(--liwe3-light-error);
    --liwe3-paper: var(--liwe3-light-mode3-400);
    --liwe3-lighter-paper: var(--liwe3-light-mode3-200);
    --liwe3-darker-paper: var(--liwe3-light-mode3-500);
    --liwe3-border-color: var(--liwe3-light-mode1-500-border);
  }
  ```

- **Dark Theme Colors**:

  ```css
  .liwe3-dark-theme {
    --liwe3-primary-color: var(--liwe3-dark-mode1-500);
    --liwe3-lighter-primary-color: var(--liwe3-dark-mode1-300);
    --liwe3-darker-primary-color: var(--liwe3-dark-mode1-700);
    --liwe3-secondary-color: var(--liwe3-dark-mode2-500);
    --liwe3-lighter-secondary-color: var(--liwe3-dark-mode2-300);
    --liwe3-darker-secondary-color: var(--liwe3-dark-mode2-700);
    --liwe3-tertiary-color: var(--liwe3-dark-mode3-500);
    --liwe3-lighter-tertiary-color: var(--liwe3-dark-mode3-300);
    --liwe3-darker-tertiary-color: var(--liwe3-dark-mode3-700);
    --liwe3-accent-color: var(--liwe3-dark-mode4-500);
    --liwe3-lighter-accent-color: var(--liwe3-dark-mode4-300);
    --liwe3-darker-accent-color: var(--liwe3-dark-mode4-700);
    --liwe3-background: var(--liwe3-dark-background-color);
    --liwe3-color: var(--liwe3-dark-text-color);
    --liwe3-link-color: var(--liwe3-dark-link-color);
    --liwe3-link-hover-color: var(--liwe3-dark-link-500-hover);
    --liwe3-link-active-color: var(--liwe3-dark-link-500-active);
    --liwe3-link-visited-color: var(--liwe3-dark-link-500-active);
    --liwe3-link-disabled-color: var(--liwe3-dark-link-500-disabled);
    --liwe3-info-color: var(--liwe3-dark-info);
    --liwe3-success-color: var(--liwe3-dark-success);
    --liwe3-warning-color: var(--liwe3-dark-warning);
    --liwe3-error-color: var(--liwe3-dark-error);
    --liwe3-paper: var(--liwe3-dark-mode3-400);
    --liwe3-lighter-paper: var(--liwe3-dark-mode3-200);
    --liwe3-darker-paper: var(--liwe3-dark-mode3-500);
    --liwe3-border-color: var(--liwe3-dark-mode1-500-border);
  }
  ```

- **Scheme Colors**:

  ```css
  .liwe3-paper {
    background-color: var(--liwe3-paper);
    color: var(--liwe3-color);
    padding: var(--liwe3-space-3);
    border-radius: var(--liwe3-border-radius);
    box-shadow: 0 0 3px 0 rgba(0, 0, 0, 0.1);
  }

  .liwe3-scheme-primary {
    background-color: var(--liwe3-primary-color);
    color: var(--liwe3-default-color);
  }

  .liwe3-scheme-secondary {
    background-color: var(--liwe3-secondary-color);
    color: var(--liwe3-default-color);
  }

  .liwe3-scheme-success {
    background-color: var(--liwe3-success-color);
    color: var(--liwe3-secondary-color);
  }

  .liwe3-scheme-danger {
    background-color: var(--liwe3-error-color);
    color: var(--liwe3-default-color);
  }

  .liwe3-scheme-warning {
    background-color: var(--liwe3-warning-color);
    color: var(--liwe3-default-color);
  }

  .liwe3-scheme-info {
    background-color: var(--liwe3-info-color);
    color: var(--liwe3-default-color);
  }

  .liwe3-scheme-dark {
    background-color: var(--liwe3-dark-color);
    color: var(--liwe3-light-color);
  }

  .liwe3-scheme-light {
    background-color: var(--liwe3-light-color);
    color: var(--liwe3-dark-color);
  }

  .liwe3-scheme-alternative {
    background-color: var(--liwe3-alternative-color);
    color: var(--liwe3-default-color);
  }
  ```
