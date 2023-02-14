def test_user_device_association(user_factory, device_factory):
    user = user_factory()
    device = device_factory(user=user)

    # Your test assertions go here
    assert user.devices == [device]
    assert device.user == user
