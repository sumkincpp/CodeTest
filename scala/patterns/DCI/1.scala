case class Account(account: String, balance: Float)

class Transfer(src: Account, dest: Account, amount: Float) {
  private val source = src.as[Source]
  private val destination = dest.as[Destination]

  def transfer() {
    source.transfer
  }

  private trait Source {self: Account =>
    def withdraw() {
      balance -= amount
    }

    def transfer() {
      destination.deposit()
      withdraw()
    }
  }

  private trait Destination {self: Account =>
    def deposit() {
      balance += amount
    }
  }
}

// and then just do something like:

new Transfer(Account("foo", 100.00), Account("bar", 50.00), 42.42).transfer()
