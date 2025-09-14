declare module 'react-signature-canvas' {
  import * as React from 'react';

  export interface SignatureCanvasProps {
    penColor?: string;
    canvasProps?: React.CanvasHTMLAttributes<HTMLCanvasElement>;
    clearOnResize?: boolean;
  }

  class SignatureCanvas extends React.Component<SignatureCanvasProps> {
    clear(): void;
    getTrimmedCanvas(): HTMLCanvasElement;
    toDataURL(): string;
  }

  export default SignatureCanvas;
}
