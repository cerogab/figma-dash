# PulseCRM — Figma Design Spec & Brief

> A structured spec to manually build every screen in Figma.
> Frame size: **iPhone 15 Pro — 393 x 852pt**

---

## 1. Design Tokens (Create a "Design System" page first)

### Colors
| Name | Hex | Usage |
|---|---|---|
| **Primary** | `#6C63FF` | Buttons, icons, accents, tab tint, links |
| **Primary Light** | `#6C63FF` at 10% opacity | Icon circle backgrounds, chip highlights |
| **Background** | `#F5F5F7` | App background (every screen) |
| **Card** | `#FFFFFF` | All card/container fills |
| **Text Primary** | `#1A1A2E` | Headings, names, primary labels |
| **Text Secondary** | `#6B7280` | Subtitles, descriptions, timestamps |
| **Success** | `#34C759` | "Converted" badge, call button tint |
| **Warning** | `#FF9500` | "Contacted" badge |
| **Error** | `#FF3B30` | "Lost" badge, destructive actions |
| **Info Blue** | `#007AFF` | "Qualified" badge |
| **White** | `#FFFFFF` | Button text on purple, card fills |
| **Divider** | `#E5E7EB` | Separator lines |

### Typography (SF Pro — system default)
| Style | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| Large Title | 34pt | Bold | 41pt | Login title |
| Title 2 | 22pt | Semibold | 28pt | Screen headings, greeting |
| Headline | 17pt | Semibold | 22pt | Card titles, contact names |
| Body | 17pt | Regular | 22pt | Form fields, descriptions |
| Subheadline | 15pt | Regular | 20pt | Card subtitles, company names |
| Caption 1 | 12pt | Medium | 16pt | Badges, timestamps, labels |

### Spacing Scale
| Token | Value |
|---|---|
| xxs | 4pt |
| xs | 8pt |
| sm | 12pt |
| md | 16pt |
| lg | 24pt |
| xl | 32pt |
| xxl | 48pt |

### Corner Radius
| Element | Radius |
|---|---|
| Cards | 16pt |
| Buttons | 12pt |
| Badges/Chips | 8pt |
| Input Fields | 10pt |
| Icon Circles | Full (50%) |

### Shadows
| Element | Settings |
|---|---|
| Cards | Color: `#000000` at 5% opacity, X: 0, Y: 2, Blur: 8 |
| Elevated buttons | Color: `#6C63FF` at 20% opacity, X: 0, Y: 4, Blur: 12 |

---

## 2. Component Library (Build these as Figma Components)

### 2A. PrimaryButton
- **Size:** Full-width, height 50pt
- **Fill:** `#6C63FF`
- **Text:** 17pt Semibold, `#FFFFFF`, centered
- **Radius:** 12pt
- **State variants:** Default, Pressed (darken 10%), Disabled (50% opacity)

### 2B. AppTextField
- **Layout:** Vertical stack
  - Label: 12pt Medium, `#6B7280`, above field, 4pt gap
  - Field: Full-width, height 44pt, fill `#FFFFFF`, border 1pt `#E5E7EB`, radius 10pt
  - Inner text: 17pt Regular, `#1A1A2E`, left-padded 12pt
  - Placeholder: 17pt Regular, `#6B7280` at 50%
- **State variants:** Default, Focused (border `#6C63FF`), Error (border `#FF3B30`)

### 2C. CardContainer
- **Fill:** `#FFFFFF`
- **Radius:** 16pt
- **Padding:** 16pt all sides
- **Shadow:** Card shadow (see above)
- **Auto Layout:** Vertical, spacing varies per usage

### 2D. StatusBadge
- **Layout:** Auto Layout, horizontal, padding 6pt vertical / 10pt horizontal
- **Radius:** 8pt
- **Text:** 12pt Medium, white
- **Variants by status:**
  - New → fill `#6C63FF`
  - Contacted → fill `#FF9500`
  - Qualified → fill `#007AFF`
  - Converted → fill `#34C759`
  - Lost → fill `#FF3B30`

### 2E. QuickActionCard
- **Size:** Flexible width (2-column grid, ~174pt each with 16pt gap)
- **Fill:** `#FFFFFF`, radius 16pt, card shadow
- **Layout:** Vertical Auto Layout, center-aligned, padding 24pt vertical / 16pt horizontal
  - Icon circle: 56x56pt, fill `#6C63FF` at 10%, icon 28pt in `#6C63FF`
  - Gap: 12pt
  - Label: 15pt Medium, `#1A1A2E`

### 2F. ContactCard
- **Container:** CardContainer
- **Layout:** Vertical Auto Layout, spacing 12pt
  - **Row 1:** HStack
    - Left: VStack — Name (17pt Semibold, `#1A1A2E`) + Company (15pt Regular, `#6B7280`)
    - Right: StatusBadge
  - **Row 2:** HStack, spacing 12pt
    - Call Button: 40x40pt circle, fill `#34C759` at 10%, phone icon 18pt `#34C759`
    - Email Button: 40x40pt circle, fill `#6C63FF` at 10%, envelope icon 18pt `#6C63FF`

### 2G. FilterChip
- **Layout:** Auto Layout, horizontal, padding 8pt vertical / 16pt horizontal
- **Radius:** 20pt (pill shape)
- **Variants:**
  - Inactive: fill `#FFFFFF`, border 1pt `#E5E7EB`, text 14pt Medium `#6B7280`
  - Active: fill `#6C63FF`, no border, text 14pt Medium `#FFFFFF`

### 2H. TabBar
- **Position:** Fixed bottom
- **Size:** 393 x 83pt (includes safe area)
- **Fill:** `#FFFFFF`, top border 0.5pt `#E5E7EB`
- **4 tabs**, equal spacing, each:
  - Icon: 24pt, inactive `#6B7280`, active `#6C63FF`
  - Label: 10pt Medium, inactive `#6B7280`, active `#6C63FF`
  - Tabs: Home (`house.fill`), Contacts (`person.2.fill`), Trends (`chart.line.uptrend.xyaxis`), Settings (`gearshape.fill`)

### 2I. SearchBar
- **Size:** Full-width, height 36pt
- **Fill:** `#E5E7EB` at 50%, radius 10pt
- **Leading icon:** magnifying glass 16pt `#6B7280`, left-padded 8pt
- **Placeholder text:** "Search contacts..." 15pt Regular `#6B7280`

---

## 3. Screen-by-Screen Specs

---

### Screen 1: Login

**Frame:** 393 x 852pt, fill `#F5F5F7`

**Layout (centered VStack, spacing 24pt, horizontal padding 32pt):**

1. **App Logo** — 72x72pt placeholder square, `#6C63FF` fill, radius 16pt (centered)
2. **Gap:** 8pt
3. **App Name** — "PulseCRM" — 34pt Bold, `#6C63FF`, centered
4. **Tagline** — "Your business, amplified." — 15pt Regular, `#6B7280`, centered
5. **Gap:** 32pt
6. **Email Field** — `AppTextField`, label "Email", placeholder "admin@pulsecrm.com"
7. **Gap:** 16pt
8. **Password Field** — `AppTextField`, label "Password", placeholder "Enter password", obscured dots
9. **Gap:** 24pt
10. **Sign In Button** — `PrimaryButton`, text "Sign In"
11. **Gap:** 16pt
12. **Divider row** — line + "or" text + line (text 12pt Medium `#6B7280`)
13. **Gap:** 16pt
14. **Biometric Button** — HStack: Face ID icon (SF Symbol `faceid`) 22pt `#6C63FF` + "Sign in with Face ID" 15pt Medium `#6C63FF`

---

### Screen 2: Home

**Frame:** 393 x 852pt, fill `#F5F5F7`

**Layout (ScrollView, padding 16pt horizontal, 24pt top):**

1. **Greeting Section** — VStack, left-aligned
   - "Good Morning," — 22pt Semibold, `#6B7280`
   - "Diego" — 28pt Bold, `#1A1A2E`
   - Gap: 4pt
   - "Here's your business at a glance" — 15pt Regular, `#6B7280`
2. **Gap:** 32pt
3. **Quick Actions Grid** — 2-column grid, 16pt gap
   - Card 1: icon `person.2.fill` → "CRM Contacts"
   - Card 2: icon `chart.line.uptrend.xyaxis` → "Trends"
   - Card 3: icon `plus.circle.fill` → "Add Client"
   - (Card 4 optional or leave empty for asymmetry)

**Bottom:** TabBar (Home tab active)

---

### Screen 3: CRM Contacts

**Frame:** 393 x 852pt, fill `#F5F5F7`

**Layout:**

1. **Nav Title** — "Contacts" — 34pt Bold, `#1A1A2E` (large title style), left-aligned, padding 16pt
2. **Search Bar** — full width, horizontal padding 16pt
3. **Gap:** 12pt
4. **Filter Chips Row** — Horizontal scroll, padding-left 16pt, 8pt gaps between chips
   - Chips: "All" (active), "New", "Contacted", "Qualified", "Converted", "Lost"
5. **Gap:** 16pt
6. **Contact List** — Vertical stack, spacing 12pt, padding 16pt horizontal
   - **ContactCard** × 8 sample entries:
     - Sarah Johnson / TechVision Inc / Converted
     - Michael Chen / DataFlow Systems / Contacted
     - Emily Rodriguez / GreenLeaf Marketing / New
     - James Wilson / Atlas Consulting / Qualified
     - Priya Patel / NovaByte Labs / Lost
     - David Kim / Summit Digital / Contacted
     - Lisa Thompson / BrightPath Education / New
     - Robert Martinez / ClearView Analytics / Converted
7. **FAB (Floating Action Button)** — Bottom-right, 56x56pt, fill `#6C63FF`, "+" icon 24pt white, radius full circle, elevated shadow

**Bottom:** TabBar (Contacts tab active)

---

### Screen 4: Add Client (Sheet/Modal)

**Frame:** 393 x ~700pt (sheet, partial overlay, top radius 16pt)

**Layout:**

1. **Handle bar** — 36x5pt, `#E5E7EB`, radius 3pt, centered, top margin 8pt
2. **Header row** — HStack, padding 16pt
   - "Cancel" text button — 17pt Regular, `#6C63FF`
   - Center: "New Client" — 17pt Semibold, `#1A1A2E`
   - "Save" text button — 17pt Semibold, `#6C63FF`
3. **Divider** — 0.5pt `#E5E7EB`
4. **Form** — Vertical stack, padding 16pt, spacing 20pt
   - `AppTextField` — label "Full Name", placeholder "Enter name"
   - `AppTextField` — label "Company", placeholder "Company name"
   - `AppTextField` — label "Phone", placeholder "+1 (555) 000-0000"
   - `AppTextField` — label "Email", placeholder "email@company.com"
   - **Status Picker** — label "Status" (12pt Medium `#6B7280`), row of 5 `FilterChip`s: New (active), Contacted, Qualified, Converted, Lost
   - **Notes** — label "Notes", text area 100pt height, fill `#FFFFFF`, border 1pt `#E5E7EB`, radius 10pt

---

### Screen 5: Analytics / Trends

**Frame:** 393 x 852pt, fill `#F5F5F7`

**Layout (ScrollView, padding 16pt horizontal, 24pt top):**

1. **Nav Title** — "Trends" — 34pt Bold, `#1A1A2E`, left-aligned
2. **Gap:** 16pt
3. **Time Range Picker** — Segmented control, full-width
   - 4 segments: "Week", "Month", "Quarter", "Year"
   - Active: fill `#6C63FF`, text white 14pt Semibold
   - Inactive: fill `#FFFFFF`, text `#6B7280` 14pt Medium
   - Container: `#E5E7EB` fill, radius 8pt, height 36pt
4. **Gap:** 24pt
5. **Outreach Chart Card** — CardContainer
   - Title: "Outreach Performance" — 17pt Semibold, `#1A1A2E`
   - Subtitle: "Emails & calls over time" — 13pt Regular, `#6B7280`
   - Gap: 16pt
   - **Line Chart** — 200pt height
     - Line color: `#6C63FF`, 2pt stroke
     - Area fill: gradient from `#6C63FF` at 30% → transparent
     - X-axis: date labels, Y-axis: numbers
     - Data dots: 6pt circles, fill `#6C63FF`, white 2pt border
6. **Gap:** 16pt
7. **Conversion Chart Card** — CardContainer
   - Title: "Conversion Trends" — 17pt Semibold, `#1A1A2E`
   - Gap: 16pt
   - **Bar Chart** — 200pt height
     - Bar fill: `#6C63FF` gradient (lighter at top)
     - Bar width: ~30pt, radius top-left/right 6pt
     - X-axis: "Jan", "Feb", "Mar", "Apr", "May", "Jun"
     - Y-axis: numbers
8. **Gap:** 16pt
9. **Response Rate Card** — CardContainer, HStack
   - Left: "Response Rate" label 15pt Medium `#6B7280` + "68%" in 34pt Bold `#1A1A2E`
   - Right: Green up-arrow icon + "+12% from last month" 13pt Medium `#34C759`

**Bottom:** TabBar (Trends tab active)

---

### Screen 6: Settings

**Frame:** 393 x 852pt, fill `#F5F5F7`

**Layout:**

1. **Nav Title** — "Settings" — 34pt Bold, `#1A1A2E`, left-aligned, padding 16pt
2. **Gap:** 24pt
3. **Profile Card** — CardContainer, horizontal padding 16pt
   - HStack:
     - Avatar circle: 56x56pt, fill `#6C63FF` at 15%, initials "D" in 24pt Bold `#6C63FF`
     - Gap: 12pt
     - VStack: "Diego" 17pt Semibold `#1A1A2E` + "admin@pulsecrm.com" 15pt Regular `#6B7280`
4. **Gap:** 24pt
5. **Menu List** — CardContainer, vertical stack
   - Row: "Account" — icon `person.circle` + label 17pt Regular + chevron right
   - Divider
   - Row: "Notifications" — icon `bell` + label + chevron
   - Divider
   - Row: "Appearance" — icon `paintbrush` + label + chevron
6. **Gap:** 16pt
7. **Logout Card** — CardContainer
   - Row: "Log Out" — icon `rectangle.portrait.and.arrow.right` `#FF3B30` + label 17pt Medium `#FF3B30`, centered
8. **Gap:** 24pt
9. **Footer** — "PulseCRM v1.0.0" — 12pt Regular, `#6B7280`, centered

**Bottom:** TabBar (Settings tab active)

---

## 4. SF Symbol Icon Reference

| Usage | SF Symbol Name |
|---|---|
| Home tab | `house.fill` |
| Contacts tab | `person.2.fill` |
| Trends tab | `chart.line.uptrend.xyaxis` |
| Settings tab | `gearshape.fill` |
| Search | `magnifyingglass` |
| Call button | `phone.fill` |
| Email button | `envelope.fill` |
| Add client FAB | `plus` |
| Add client card | `plus.circle.fill` |
| Face ID | `faceid` |
| Chevron right | `chevron.right` |
| Up trend arrow | `arrow.up.right` |
| Logout | `rectangle.portrait.and.arrow.right` |
| Account | `person.circle` |
| Notifications | `bell` |
| Appearance | `paintbrush` |

> **Tip:** Download the [SF Symbols app](https://developer.apple.com/sf-symbols/) and drag icons directly into Figma, or use the [SF Symbols Figma plugin](https://www.figma.com/community/plugin/1207616473498503989/sf-symbols).

---

## 5. Figma Build Order

1. **Page 1 — Design System:** Color swatches, typography samples, spacing scale, shadow samples, all 9 components
2. **Page 2 — Login Screen**
3. **Page 3 — Home Screen**
4. **Page 4 — Contacts Screen** + Add Client sheet as overlay variant
5. **Page 5 — Analytics/Trends Screen**
6. **Page 6 — Settings Screen**
7. **Page 7 — Component Variants** (StatusBadge ×5, FilterChip ×2, Button states ×3, TextField states ×3, TabBar active states ×4)

---

## 6. Figma Pro Tips

- **Use Figma Variables** for all colors and spacing tokens — makes global changes instant
- **Use Auto Layout** on every frame — matches how SwiftUI stacks work (VStack = vertical AL, HStack = horizontal AL)
- **Create components with variants** for StatusBadge, FilterChip, Button, TextField — swap states easily
- **Use the "iOS 17" Figma UI Kit** from Apple's design resources as a reference for native elements (tab bar, navigation bar, segmented controls)
- **Name layers** to match the component names in this spec (e.g., "ContactCard", "StatusBadge/Converted") for clean handoff

---

## 7. Verification Checklist

- [ ] All screens use only the tokens defined in Section 1
- [ ] Every component has defined states/variants
- [ ] All text uses SF Pro at specified sizes and weights
- [ ] All icons match the SF Symbol names in Section 4
- [ ] Cards use consistent 16pt padding, 16pt radius, and card shadow
- [ ] Tab bar is identical across all 4 main screens with correct active highlight
- [ ] Frames are all 393 x 852pt (iPhone 15 Pro)
- [ ] Auto Layout is used on all containers (no fixed positioning except FAB and TabBar)
