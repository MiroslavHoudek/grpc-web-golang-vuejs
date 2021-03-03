export class TodoList {
  async getTodoList () {
    const req = new this.proto.Empty()
    // req.setEmail(user.email.trim().toLowerCase())
    // req.setPassword(user.password.trim())
    const res = await this.client.getTodoList(req, {})
    // const state = res
    // localStorage.setItem(this.state, res)
    return res
  }

  constructor (deps) {
    this.tokenKey = deps.tokenKey
    this.proto = deps.proto
    this.client = new deps.proto.TodoClient(process.env.API_URL, null, null)
  }

  logout () {
    localStorage.removeItem(this.tokenKey)
  }
}
