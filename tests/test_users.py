def test_user_device_association(UserFactory, DeviceFactory):
    user = UserFactory()
    device = DeviceFactory(user=user)

    # Your test assertions go here
    assert user.devices == [device]
    assert device.user == user
