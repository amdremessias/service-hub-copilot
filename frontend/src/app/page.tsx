export default function Home() {
  return (
    <main className="flex items-center justify-center min-h-screen">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-dark mb-4">Service Hub</h1>
        <p className="text-lg text-gray-600 mb-8">SaaS Marketplace de Técnicos e Serviços</p>
        <div className="space-x-4">
          <a href="/auth/login" className="btn-primary inline-block">
            Entrar
          </a>
          <a href="/auth/register" className="btn-secondary inline-block">
            Registrar
          </a>
        </div>
      </div>
    </main>
  );
}
