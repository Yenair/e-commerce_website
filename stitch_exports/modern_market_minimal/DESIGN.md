---
name: Modern Market Minimal
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#a73a00'
  on-secondary: '#ffffff'
  secondary-container: '#fd651e'
  on-secondary-container: '#571a00'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00201d'
  on-tertiary-container: '#0c9488'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb599'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#7f2b00'
  tertiary-fixed: '#89f5e7'
  tertiary-fixed-dim: '#6bd8cb'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#005049'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-hero:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.03em
  display-hero-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.025em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 26px
    fontWeight: '700'
    lineHeight: 34px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  price-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: -0.02em
  price-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 3rem
  margin-tablet: 2rem
  margin-mobile: 1rem
  space-2xs: 0.25rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
  space-3xl: 4rem
---

## Brand & Style

This design system establishes a high-clarity, elevated retail experience for a modern grocery and everyday goods platform. Built on the principles of refined utility and deliberate restraint, it transforms mundane basket-building into an intuitive, frictionless digital routine.

### Brand Personality & Emotional Core
- **Effortless Precision:** Fast, systematic scanning paired with direct, high-confidence interactions.
- **Warm Domesticity:** Approachable, fresh, and trustworthy—balancing grocery utility with boutique digital craftsmanship.
- **Uncluttered Calm:** Eliminates visual fatigue and retail sensory overload through generous negative space, intentional hierarchy, and calm surface tones.

### Design Movement: Warm Modernist Minimalism
The visual language merges crisp structural order with gentle tactile ergonomics:
- **Architectural Clarity:** Layouts favor strict horizontal rhythm, deliberate vertical cadence, and silent structural dividers over loud borders.
- **Curated Accents:** Color is never decorative; it denotes active pathways, critical deals, and completion states.
- **Physical Softness:** Generous corner radii (`rounded-xl` to `rounded-2xl`) and gentle ambient depth offset mechanical grid structures, evoking physical pantry packaging and tactile store shelves.

## Colors

The palette balances deep nautical authority with high-visibility appetite cues and crisp, hygienic neutrals.

### Roles & Semantic Distribution
- **Primary (`#0F172A` - Midnight Slate):** Used for typography anchors, core navigation bars, primary structural headers, and grounded interactive states.
- **Secondary (`#EA580C` - Vibrant Tangerine):** The primary conversion vehicle. Reserved strictly for primary action drivers (Add to Cart, Checkout, dynamic pricing tags, limited promotions, and badge highlights).
- **Tertiary (`#0D9488` - Crisp Teal):** Functional semantic role for freshness markers (organic certifications, dietary badges, express delivery indicators, and stock confirmations).
- **Neutral Canvas (`#F8FAFC` to `#FFFFFF`):** A stepped neutral ladder providing layered relief:
  - Base Background: `#F8FAFC` (Slate Tint)
  - Card & Flyout Surfaces: `#FFFFFF` (Crisp Warm White)
  - Muted Borders & Structural Separators: `#E2E8F0`
  - Subtle Insets & Secondary Fill: `#F1F5F9`
  - Body Copy & Secondary Text: `#475569` (Slate Midtone)

## Typography

Plus Jakarta Sans is utilized across all typographic roles. Its clean geometry delivers high-efficiency scannability, while its gentle terminal curvature softens information density.

### Type Rules & Implementation Details
- **Tight Headings:** High negative letter-spacing (`-0.02em` to `-0.03em`) on titles prevents visual looseness and anchors rapid aisle/category scanning.
- **Price Treatment:** Numeric price displays are always rendered in `Plus Jakarta Sans` with `font-variant-numeric: tabular-nums` to eliminate layout shift during rapid quantity modification.
- **Hierarchy Enforcers:** Product descriptions utilize `body-sm` (`#475569`), preserving high contrast for headline titles and primary action pricing badges.

## Layout & Spacing

The layout model relies on an expansive 12-column responsive fluid grid pinned to a strict maximum content container of 1440px.

### Grid Rhythm & Device Breakpoints
- **Desktop (1024px+):** 12-column layout, `3rem` margins, `1.5rem` gutters. Product feeds default to 4-column or 6-column arrangements.
- **Tablet (768px - 1023px):** 8-column layout, `2rem` margins, `1.25rem` gutters. Product grids condense to 3 columns.
- **Mobile (0px - 767px):** 4-column layout, `1rem` margins, `1rem` gutters. Product displays reflow to a 2-column compact grid or continuous horizontal carousels.

### Spacing Principles
- **Micro-Gaps (`space-2xs` to `space-xs`):** Exclusively reserved for inline meta-labels, ratings stars, unit labels, and badge padding.
- **Component Padding (`space-sm` to `space-lg`):** Product card internal margins, form field padding, and floating control spacing.
- **Macro Separators (`space-xl` to `space-3xl`):** Vertical buffer between distinct merchandising aisles, banner takeovers, and cart summary modules.

## Elevation & Depth

Visual hierarchy leverages ambient, diffused light rather than opaque, stacked surfaces. This approach maintains a lightweight, tactile feel across all catalog tiers.

### Depth Archetypes
- **Base Level (Canvas):** Flat `#F8FAFC`. Completely un-elevated surface for general browsing ground.
- **Level 1 (Card & Module Resting):** Pure `#FFFFFF` background supported by a hairline border (`1px solid #E2E8F0`) and an ambient tinted drop shadow:
  - `0 1px 3px 0 rgba(15, 23, 42, 0.04), 0 1px 2px -1px rgba(15, 23, 42, 0.02)`
- **Level 2 (Hover & Active Product Cards):** Triggered on desktop cursor hover:
  - Transform lift: `translateY(-3px)`
  - Shadow bloom: `0 12px 24px -6px rgba(15, 23, 42, 0.08), 0 4px 8px -2px rgba(15, 23, 42, 0.03)`
  - Border transition: `#CBD5E1`
- **Level 3 (Flyouts, Quick-Carts & Sticky Nav):**
  - High-diffusion elevation: `0 20px 30px -10px rgba(15, 23, 42, 0.12), 0 8px 12px -4px rgba(15, 23, 42, 0.04)`
  - Frosted sticky headers apply a lightweight glass filter (`backdrop-filter: blur(12px); background-color: rgba(255, 255, 255, 0.85)`).

## Shapes

The design system uses generous, organic radii to soften transactional utility, evoking welcoming physical retail environments.

### Shape Hierarchy
- **Primary Surfaces & Cards:** Standardized on `rounded-xl` (1rem / 16px) for item cards, module containers, and banners. Large feature displays leverage `rounded-2xl` (1.5rem / 24px).
- **Controls & Form Elements:** Buttons, search fields, counter steppers, and pill badges adhere to `rounded-xl` (0.75rem to 1rem) or full organic pills (`rounded-full`) for status indicators.
- **Image Frames:** Product preview assets sit inside internal containers clipped to `0.75rem` (12px) to conform harmoniously within parent card architecture.

## Components

### Buttons
- **Primary (Action):** Background `#EA580C`, text `#FFFFFF`, font `label-lg`. Padding: `0.75rem 1.5rem`. Smooth hover to `#C2410C` with subtle `translateY(-1px)`.
- **Secondary (Utility):** Background `#0F172A`, text `#FFFFFF`. Used for critical account operations and primary navigational anchors.
- **Ghost / Outline:** Background transparent, border `1.5px solid #E2E8F0`, text `#0F172A`. Hover transitions to `#F1F5F9`.

### Product Cards
- Self-contained canvas `#FFFFFF`, `rounded-xl` geometry, `1px solid #E2E8F0`.
- Aspect-ratio locked image preview (1:1) framed with `#F8FAFC` background.
- Floating top badges: Discount tags (`#EA580C` text on `#FFEDD5` pill) and Dietary/Freshness tags (`#0D9488` text on `#CCFBF1` pill).
- Bottom interaction shelf: Tabular price left-aligned; floating circular or pill Add-to-Cart stepper right-aligned. Hover executes a 200ms cubic-bezier translation.

### Chips & Category Filters
- Compact selector pills with `rounded-full` boundaries.
- **Resting:** Inset `#F1F5F9`, text `#475569`, border `1px solid transparent`.
- **Selected:** Background `#0F172A`, text `#FFFFFF`, font `label-md`.

### Form Fields & Search Input
- Prominent omni-search input featuring deep slate placeholder text (`#94A3B8`), `rounded-xl` enclosure, and hairline `#E2E8F0` resting border.
- Active focus state: Clean focus ring `0 0 0 3px rgba(234, 88, 12, 0.15)` paired with `#EA580C` border transition.

### Quantity Stepper (Pantry Counter)
- Ergonomic horizontal capsule (`rounded-full`) containing minus, text-counter, and plus triggers.
- Replaces standard Add-to-Cart button upon first selection to streamline basket-building without opening modal drawers.

### Checkboxes & Radio Controls
- Base: `1.25rem` square (checkbox, `rounded-md`) or circle (radio).
- Inactive: `#FFFFFF` with `1.5px solid #CBD5E1`.
- Checked: `#EA580C` fill with clean white interior glyph, transitioning smoothly via `cubic-bezier(0.4, 0, 0.2, 1)`.