import { createContext, useState, ReactNode, useEffect } from 'react';

type ThemeContextType = {
  theme: string,
  toggleTheme: () => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined)